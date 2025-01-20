#!/usr/bin/env python3
from z3 import *
import sys
from Crypto.Util.strxor import strxor

def apply_initial_state_z3(x):
    x = x ^ ((x << 31) & 0xFFFFFFFFFFFFFFFF)
    x = x ^ LShR(x, 19)
    x = x ^ ((x << 13) & 0xFFFFFFFFFFFFFFFF)
    return x & 0xFFFFFFFFFFFFFFFF

def solve_dual_xorshift(ciphertext_hex):
    ct_bytes = bytes.fromhex(ciphertext_hex)
    total_len = len(ct_bytes)
    key_part_len = 2 * (total_len // 3)
    s0 = BitVec('s0', 64)
    s1 = BitVec('s1', 64)
    solver = Solver()
    blocks = (total_len + 7) // 8
    states_s0 = [s0]
    states_s1 = [s1]
    keystreams = []
    for i in range(blocks):
        ns0 = apply_initial_state_z3(states_s0[-1])
        ns1 = apply_initial_state_z3(states_s1[-1])
        states_s0.append(ns0)
        states_s1.append(ns1)
        keystreams.append(ns0 ^ ns1)
    for i in range(blocks):
        start = i * 8
        end = min(start + 8, total_len)
        block_size = end - start
        block_val = 0
        for j, b in enumerate(ct_bytes[start:end]):
            block_val |= (b << (8 * j))
        pt_block = keystreams[i] ^ block_val
        for j in range(block_size):
            idx = start + j
            if idx < key_part_len:
                byte_j = Extract(8*j+7, 8*j, pt_block)
                solver.add(Or(
                    And(byte_j >= 0x30, byte_j <= 0x39),
                    And(byte_j >= 0x61, byte_j <= 0x66)
                ))
    if solver.check() != sat:
        print("No solution")
        return
    model = solver.model()
    s0_val = model[s0].as_long()
    s1_val = model[s1].as_long()
    p = bytearray(total_len)
    def apply_initial_state_py(x):
        x ^= (x << 31) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> 19) & 0xFFFFFFFFFFFFFFFF
        x ^= (x << 13) & 0xFFFFFFFFFFFFFFFF
        return x & 0xFFFFFFFFFFFFFFFF
    st0 = s0_val
    st1 = s1_val
    for i in range(blocks):
        st0 = apply_initial_state_py(st0)
        st1 = apply_initial_state_py(st1)
        k = st0 ^ st1
        start = i * 8
        end = min(start + 8, total_len)
        block_val = 0
        for j, b in enumerate(ct_bytes[start:end]):
            block_val |= (b << (8 * j))
        dec_block = (block_val ^ k).to_bytes(8, 'little')
        for j in range(end - start):
            p[start + j] = dec_block[j]
    key_hex_part = p[:key_part_len]
    xored_flag_part = p[key_part_len:]
    real_key = bytes.fromhex(key_hex_part.decode())
    recovered_flag = strxor(real_key, xored_flag_part)
    print(real_key.hex())
    print(recovered_flag.decode(errors='replace'))

def main():
    if len(sys.argv) != 2:
        print("Usage: solve.py <hex_ciphertext>")
        return
    solve_dual_xorshift(sys.argv[1])

if __name__ == "__main__":
    main()

