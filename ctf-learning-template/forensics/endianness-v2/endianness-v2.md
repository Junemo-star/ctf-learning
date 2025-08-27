# picoCTF – Endian Challenge

## 🔍 คำอธิบาย
เราได้รับไฟล์ที่กู้มาจากระบบ 32-bit ซึ่งมีการจัดเรียงไบต์แบบแปลก ๆ  
ข้อความโจทย์บอกว่า:

> "นี่คือไฟล์ที่กู้มาจากระบบ 32-bits ที่จัดเรียงไบต์แบบแปลก ๆ เราไม่แน่ใจว่าไฟล์นี้เป็นประเภทอะไร"

เมื่อใช้คำสั่ง `file` ตรวจสอบ พบว่าเป็นเพียง `data` ไม่สามารถบอกชนิดไฟล์ได้

---

## 🛠️ ขั้นตอนการทำ

### 1. ตรวจสอบชนิดไฟล์
```bash
file challengefile
```

ผลลัพธ์

```
challengefile: data
```
### 2. เปิดดู header ด้วย hex
```
xxd challengefile | head
```

พบว่า header คล้าย JPEG (FFD8 FFE0 ... JFIF) แต่ไบต์เรียงผิด:

### 3. วิเคราะห์
จากที่โจทย์บอกว่าเป็นระบบ 32-bit และ header เพี้ยน → ไฟล์น่าจะถูกสลับ endian

ลองสลับทีละ 2 byte (byte swap ทั้งไฟล์)
```
dd if=challengefile of=fixed_byteswap.jpg conv=swab
```

ลองสลับทีละ 4 byte (32-bit word swap)
```
data = open("challengefile", "rb").read()
fixed = b"".join(data[i:i+4][::-1] for i in range(0, len(data), 4))
open("fixed4.jpg", "wb").write(fixed)
```

ลองสลับแบบผสม (swap 16-bit, แล้วในแต่ละ word ก็สลับ byte)
```
data = open("challengefile", "rb").read()
fixed = bytearray()
for i in range(0, len(data), 2):
    fixed += data[i:i+2][::-1]  # swap ในแต่ละ 2 byte
open("fixed2.jpg", "wb").write(fixed)
```
จะได้มาเป็นไฟล์ fixed.jpg , fixed2.jpg , fixed4.jpg

ซึ่งพอเอามาเช็คด้วย binwalk แต่ละไฟล์แล้วพบว่า fixed4.jpg คือไฟล์ที่ถูกต้อง(ใช้ swap 16-bit, แล้วในแต่ละ word ก็สลับ byte)