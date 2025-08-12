#!/usr/bin/env python3
from pwn import *
import json

context.log_level = "debug"   # ดูทราฟฟิก
HOST, PORT = "socket.cryptohack.org", 11112

def json_recv(conn):
    line = conn.readline()
    return json.loads(line.decode())

def json_send(conn, obj):
    raw = json.dumps(obj).encode()
    print("SENDING:", raw)
    conn.sendline(raw)

r = remote(HOST, PORT)

# อ่านแบนเนอร์ (จะมีกี่บรรทัดก็ได้ ไม่ซีเรียส)
for _ in range(4):
    try:
        print(r.readline().decode().rstrip())
    except EOFError:
        break

json_send(r, {"buy": "flag"})
resp = json_recv(r)
print("RESPONSE:", resp)

r.close()
