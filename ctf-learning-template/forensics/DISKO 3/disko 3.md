# Forensic Challenge - วิเคราะห์ไฟล์ .dd และ flag.gz

## แนวคิด
- ไฟล์ `.dd` คือ **disk image** ที่เก็บข้อมูลดิบของดิสก์ทั้งก้อน  
- เป้าหมายของการโจทย์คือการ **mount และสำรวจไฟล์ภายใน** เพื่อค้นหา flag  
- Flag มักถูกซ่อนในไฟล์บีบอัด/เข้ารหัส เช่น `.gz`, `.zip`, `.rar`  
- ต้องใช้เครื่องมือ forensic + คำสั่งพื้นฐานในการดึงข้อมูลออกมา  

---

## ขั้นตอนการแก้โจทย์

### 1. unzip ไฟล์ `disko-3.dd.gz`
```bash
gzip disko-3.dd.gz
```
จะได้เป็นไฟล์ในส่วนของ disko-3.dd มาจากนั้น

### 2. Mount ไฟล์ `.dd`
```bash
sudo mount -o loop disk_image.dd /mnt
```
ทำให้เราสามารถเปิดดูไฟล์ข้างในเหมือนดิสก์จริงได้ จากนั้น เข้าไปสำรวจไฟล์

```bash
cd /mnt
ls -la
```

### 3. ค้นหาไฟล์ที่น่าสนใจ
```
find /mnt -type f -iname "*flag*"
```
ทำให้ได้เจอ flag.gz

### 4. แตกไฟล์ flag.gz
โดยปกติ
```
gunzip flag.gz
```
แต่เจอปัญหา gzip: flag: Permission denied 

แก้ปัญหาด้วยการ
```
sudo gunzip flag.gz
```
แล้วก็ได้พบกับ 
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_7e0a17da}