from PIL import Image
import numpy as np

IMG1 = r"D:\learning ctf\ctf-learning-template\ctf-crypto\CRYPTOHACK\Lemur XOR\flag_7ae18c704272532658c10b5faad06d74.png"
IMG2 = r"D:\learning ctf\ctf-learning-template\ctf-crypto\CRYPTOHACK\Lemur XOR\lemur_ed66878c338e662d3473f0d98eedbd0d.png"
OUT  = "xor_out.png"


im1 = Image.open(IMG1).convert("RGB")
im2 = Image.open(IMG2).convert("RGB")

# --- แปลงเป็นอาเรย์ uint8 แล้ว XOR ช่องสี (R,G,B) แบบพิกเซลต่อพิกเซล ---
a = np.asarray(im1, dtype=np.uint8)
b = np.asarray(im2, dtype=np.uint8)
c = np.bitwise_xor(a, b)   # เฉพาะ RGB (3 แชนเนล)

# --- เซฟผลลัพธ์เป็น PNG ---
Image.fromarray(c, mode="RGB").save(OUT)
print("saved ->", OUT)