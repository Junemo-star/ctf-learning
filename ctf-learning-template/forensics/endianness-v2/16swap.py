data = open("challengefile", "rb").read()
fixed = bytearray()
for i in range(0, len(data), 2):
    fixed += data[i:i+2][::-1]  # swap ในแต่ละ 2 byte
open("fixed2.jpg", "wb").write(fixed)
