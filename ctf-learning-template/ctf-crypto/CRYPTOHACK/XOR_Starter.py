from pwn import *

strr = b"label"
intt = 13

print(xor(strr, intt))