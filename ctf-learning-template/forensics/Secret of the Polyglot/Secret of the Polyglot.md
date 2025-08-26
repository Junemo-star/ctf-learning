เริ่มต้นจากการใช้ binwalk เพื่อดูว่ามีไฟล์อะไรอยู่บ้าง จะพบว่า 

```
0             0x0             PNG image, 50 x 50, 8-bit/color RGBA, non-interlaced
914           0x392           PDF document, version: "1.4"
1149          0x47D           Zlib compressed data, default compression
```

ทำให้รู้ว่าไฟล์ pdf นี้น่าจะมีไฟล์รูปซ่อนอยู่ จึงใช้คำสั่ง

```
dd if=mystery.pdf of=out.png bs=1 count=914
```

เนื่องจาก binwalk บอกเราว่า ไฟล์ PDF จริง ๆ เริ่มที่ offset 914 (0x392) 
ดังนั้นตั้งแต่ offset 0 จนถึงก่อน offset 914 คือ “ข้อมูล PNG” ที่ถูกฝังไว้
เราจึงใช้ count=914 เพื่อดึงข้อมูลที่ถูกฝังออกมานั่นเอง


จากนั้นก็นำข้อความที่เจอมาประกอบกันจะได้ picoCTF{f1u3n7_1n_pn9_&_pdf_249d05c0}