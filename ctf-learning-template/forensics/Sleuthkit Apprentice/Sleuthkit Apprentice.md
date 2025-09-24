
ขั้นตอนแรกใช้
```
mmls disk.flag.img
```
จะเจอ
```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```
จากนั้นลองใช้ 
```
fls -o 2048 disk.flag.img 
fls -o 360448 disk.flag.img
```
เพื่อตามหา Linux filesystem ที่เป็นอันจริงจะพบว่า 360448 นั้นเป็น Linux filesystem ตัวจริง
```
┌──(junemo㉿kali)-[~/Downloads]
└─$ fls -o 360448 disk.flag.img 
d/d 451:	home
d/d 11:	lost+found
d/d 12:	boot
d/d 1985:	etc
d/d 1986:	proc
d/d 1987:	dev
d/d 1988:	tmp
d/d 1989:	lib
d/d 1990:	var
d/d 3969:	usr
d/d 3970:	bin
d/d 1991:	sbin
d/d 1992:	media
d/d 1993:	mnt
d/d 1994:	opt
d/d 1995:	root
d/d 1996:	run
d/d 1997:	srv
d/d 1998:	sys
d/d 2358:	swap
V/V 31745:	$OrphanFiles
```
จากนั้นลอง
```
fls -o 360448 disk.flag.img 1995
```
เพื่อเข้าไปอ่านไฟล์ใน root จะพบ
```
r/r 2363:	.ash_history
d/d 3981:	my_folder
```
เราได้เจอ .ash_history (ไฟล์ history ของ shell ash (เหมือน bash history))

ดังนั้นจึงลองใช้
```
icat -o 360448 disk.flag.img 2363
------------------------------------
apk add nano
mkdir my_folder
cd my_folder/
nano flag.txt
ls -al
iconv -f ascii -t utf16 > flag.uni.txt
l
ls -al
iconv -f ascii -t utf16 flag.txt > flag.uni.txt
ls -al
shred
shred -zu flag.txt 
ls -al
halt
```
เมื่อลองใช้พบว่ามีการสร้างไฟล์ flag.txt และแปลงไฟล์ด้วย iconv เป็น UTF-16 

หลังจากนั้นไฟล์ต้นฉบับถูกลบด้วย shred -zu flag.txt = ลบ + overwrite ไฟล์ เพื่อป้องกันการกู้คืน

ดังนั้นจึงลองเข้าไปดูใน my_folder ว่ามีอะไร
```
fls -o 360448 disk.flag.img 3981
-------------------------------------
r/r * 2082(realloc):	flag.txt
r/r 2371:	flag.uni.txt
```
พบเจอไฟล์ที่ถูกลบ realloc และไฟล์ flag.uni.txt

ลอง cat ออกมาจึงเจอ flag
```
cat flag.txt 
-------------------------------
picoCTF{by73_5urf3r_2f22df38}
```