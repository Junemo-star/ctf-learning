#!/usr/bin/env python3
import sys
import re

def verify(flag: str) -> bool:
    # ปรับแพทเทิร์นให้เหมาะกับ CTF ที่คุณเล่น
    pattern = r"^flag\{[a-zA-Z0-9_\-]+\}$"
    return re.match(pattern, flag) is not None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: verify_flag.py <flag>")
        sys.exit(1)
    print("OK" if verify(sys.argv[1]) else "INVALID")
