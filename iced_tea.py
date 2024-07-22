import os
from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum

class Mode(Enum):
    ECB = 0x01
    CBC = 0x02

class Cipher:
    # ... existing code ...
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        if self.IV:
            self.mode = Mode.CBC
        else:
            self.mode = Mode.ECB
    def decrypt(self, ct):
        blocks = [ct[i:i+self.BLOCK_SIZE//8] for i in range(0, len(ct), self.BLOCK_SIZE//8)]
        
        msg = b''
        if self.mode == Mode.ECB:
            for ct_block in blocks:
                msg += self.decrypt_block(ct_block)
        elif self.mode == Mode.CBC:
            X = self.IV
            for ct_block in blocks:
                dec_block = self._xor(X, self.decrypt_block(ct_block))
                msg += dec_block
                X = ct_block
        return unpad(msg, self.BLOCK_SIZE//8)

    def decrypt_block(self, ct):
        c0 = b2l(ct[:4])
        c1 = b2l(ct[4:])
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        s = self.DELTA * 32
        for i in range(32):
            c1 -= ((c0 << 4) + K[2]) ^ (c0 + s) ^ ((c0 >> 5) + K[3])
            c1 &= msk
            c0 -= ((c1 << 4) + K[0]) ^ (c1 + s) ^ ((c1 >> 5) + K[1])
            c0 &= msk
            s -= self.DELTA
        
        m = ((c0 << (self.BLOCK_SIZE//2)) + c1) & ((1 << self.BLOCK_SIZE) - 1) # m = c0 || c1

        return l2b(m)

if __name__ == '__main__':
    KEY = bytes.fromhex(input("Enter the key in hex: "))
    CT = bytes.fromhex(input("Enter the ciphertext in hex: "))
    cipher = Cipher(KEY)
    pt = cipher.decrypt(CT)
    print(f'Plaintext : {pt}')
