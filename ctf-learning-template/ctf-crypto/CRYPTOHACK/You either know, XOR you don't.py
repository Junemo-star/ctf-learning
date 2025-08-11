from pwn import *

#key = 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

key = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

#จากโจทย์ที่ให้มา มี format เดิมอยู่นั้นคือ crypto{
known_pt = b"crypto{"

# ทำการ XOR เพื่อหาส่วนที่รู้จักของ known_pt โดยจะเอาแค่ส่วนหน้าสุดถึงส่วนความยาวของ known_pt (:len(known_pt))
key_part = xor(key[:len(known_pt)], known_pt)

#print(key_part)
# ได้ key_part = b'myXORke' จากนั้นเดา key ที่เหลือซึ่งคือ y จะได้ b'myXORkey'
full_key = b'myXORkey'

print(xor(key, full_key))

import math
print((math.gcd(66528, 52920)))