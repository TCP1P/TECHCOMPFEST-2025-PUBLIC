from sympy.crypto import *
from Crypto.Util.number import getPrime
from libnum import n2s, s2n
import signal

FLAG = open('flag.txt', 'rb').read()

params = [getPrime(1024) for _ in range(3)] + [s2n(FLAG)]
pub = kid_rsa_public_key(*params)
priv = kid_rsa_private_key(*params)

def main():
    print("--------Another baby RSA--------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("--------------------------------")
    
    choice = int(input(">>> "))
    if choice == 1:
        pt = bytes.fromhex(input("Data: "))
        pt = s2n(pt)
        ct: int = encipher_kid_rsa(pt, pub)
        print(f"Result: {n2s(ct).hex()}")
    elif choice == 2:
        ct = bytes.fromhex(input("Data: "))
        ct = s2n(ct)
        pt: int = decipher_kid_rsa(ct, priv)
        print(f"Result: {n2s(pt).hex()}")
    else: raise NotImplementedError()
    
if __name__ == '__main__':
    signal.alarm(120)
    try:
        while True: main()
    except:
        exit(1)