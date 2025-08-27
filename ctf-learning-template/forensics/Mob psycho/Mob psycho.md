# วิธีแก้โจทย์ CTF จากไฟล์ .apk

## 1. ตรวจสอบไฟล์เบื้องต้น
ใช้คำสั่ง `strings` เพื่อหาว่ามีคำว่า `flag` โผล่ในไฟล์หรือไม่

```bash
strings * | grep flag
```

เจอ path 

```
res/color/flag.txt
```

## 2. แตกไฟล์ APK
ไฟล์ .apk จริง ๆ คือไฟล์ .zip สามารถ unzip ได้โดยตรง:

```
unzip mobpsycho.apk -d output
```

ผลลัพธ์จะได้โฟลเดอร์ output/ ที่มีไฟล์ย่อย เช่น classes.dex, res/, resources.arsc

## 3. เข้าไปยัง path ที่เจอจากขั้นตอนที่ 1
```
cd output/res/color/
cat flag.txt
```

เจอข้อความ

```
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f35653637656135657d
```

จากนั้นนำไปถอดด้วย hex จะได้เป็น picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_5e67ea5e}