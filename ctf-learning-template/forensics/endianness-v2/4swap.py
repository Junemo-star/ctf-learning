data = open("challengefile", "rb").read()
fixed = b"".join(data[i:i+4][::-1] for i in range(0, len(data), 4))
open("fixed4.jpg", "wb").write(fixed)
