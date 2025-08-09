#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Template solver script

วิธีใช้:
    python3 solve.py [options]

แก้ไขตามโจทย์: อ่านไฟล์อินพุต, ถอดรหัส, แสดงผลลัพธ์
"""
import sys

def main():
    # ตัวอย่าง: ถอด XOR byte ด้วยคีย์คงที่
    # แก้ตามโจทย์จริง
    data_hex = "5a4d5c"
    key = 0x42
    data = bytes.fromhex(data_hex)
    plain = bytes([b ^ key for b in data])
    print(plain)

if __name__ == "__main__":
    main()
