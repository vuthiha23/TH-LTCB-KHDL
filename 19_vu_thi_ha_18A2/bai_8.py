ky_tu = input("nhap mot ky tu tu ban phim:")

while len(ky_tu) != 1:
    print("vui long chi nhap mot ky tu tu ban phim!")
    ky_tu = input("nhap mot ky tu tu ban phim:")
    
    
gia_tri = ord(ky_tu)

print(f"gia tri ASCII cua ky tu {ky_tu} la : {gia_tri}")

# nhap mot ky tu tu ban phim:A
# gia tri ASCII cua ky tu A la : 65