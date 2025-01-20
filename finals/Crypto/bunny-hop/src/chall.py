from functools import reduce
from typing import List
from Crypto.Util.number import getPrime
from libnum import n2s, s2n
from hashlib import md5

FLAG = open('flag.txt', 'rb').read()
n = 17
k = 384
p = getPrime(k)
q = getPrime(k)
mod = p * q

def hash(arr: List[int]) -> str:
    lhs = sum([i ** 2 for i in arr])
    rhs = reduce(lambda x, y: x * y, arr)
    if rhs:
        rhs = sum([rhs // i for i in arr])
    res = (lhs - rhs) % mod
    return md5(str(res).encode()).hexdigest()

def key_input() -> List[int]:
    s = input('Enter key: ').strip().split(';')
    assert(len(s) == n)
    assert(all([0 < int(i, 16) < mod for i in s]))
    return [int(i, 16) % mod for i in s]

def buy(choice: int) -> int:
    global mod, p, q
    if choice == 1:
        return mod
    if choice == 2:
        z = mod * mod
        return (pow(mod + 1, s2n(FLAG), z) * pow(q & 0xfedcbaabcdef, mod, z)) % z
    if choice == 3:
        return p >> (k // 2)
    if choice == 4:
        return q & (2 ** (k - 96) - 1)

def pay(choice: int) -> int:
    global balance, mod
    prices = [1, 137, 1337, 65537]
    assert(balance >= prices[choice - 1])
    balance -= prices[choice - 1]
    return buy(choice)

def adm00n():
    global balance
    res = key_input()
    h = hash(res)
    assert(h == admin_hash)
    value = min(res)
    if value in used_keys: return
    used_keys.append(value)
    balance += value.bit_length()

def menu():
    print(f'''
          --------------
          1. KFP fries (1g)
          2. FaunaMart winning lottery tickets (137g)
          3. Atlantis' trident (1337g)
          4. Ancient automaton's wind up key (65537g) 
          --------------
          Your balance: {balance}g
          ''')

balance = 0
master_key = [0] * n
admin_hash = hash(master_key)
used_keys = [0]

def main():
    menu()
    choice = int(input('>> '))
    if 1 <= choice <= 4:
        res = pay(choice)
        print(f'Checkout: {hex(res)}')
    elif choice == 0:
        print("YaG0o only!")
        adm00n()
    else:
        raise NotImplementedError()

if __name__ == '__main__':
    print("Welcome to NanaEleven!")
    try:
        while True:
            main()
    except:
        print("Bzzzt")
        exit(1)