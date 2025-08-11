import base64
#n = 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

n = input()
a = bytes.fromhex(n)
flag = base64.b64encode(a)
print(flag)

#flag = crypto/Base+64+Encoding+is+Web+Safe/