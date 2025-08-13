from pwn import remote
import json, base64, codecs
from Crypto.Util.number import long_to_bytes

HOST = "socket.cryptohack.org"
PORT = 13377

def decode_one(msg):
    t = msg["type"]
    x = msg["encoded"]

    if t == "base64":
        return base64.b64decode(x).decode()
    elif t == "hex":
        return bytes.fromhex(x).decode()
    elif t == "rot13":
        return codecs.decode(x, "rot_13")
    elif t == "bigint":
        # server เข้ารหัสด้วย: hex(bytes_to_long( ... )) -> "0x...."
        n = int(x, 16)   # แปลงกลับเป็นจำนวนเต็ม
        return long_to_bytes(n).decode()
    elif t == "utf-8":
        # เป็นลิสต์ของโค้ดพอยต์
        return ''.join(chr(c) for c in x)
    else:
        raise ValueError(f"unknown type: {t}")

def main():
    io = remote(HOST, PORT)
    while True:
        line = io.recvline()
        data = json.loads(line)

        if "flag" in data:
            print("FLAG:", data["flag"])
            break

        answer = decode_one(data)
        io.sendline(json.dumps({"decoded": answer}).encode())

if __name__ == "__main__":
    main()
