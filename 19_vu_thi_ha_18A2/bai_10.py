so = int(input("Nhap vao so thap phan: "))
chuoi_so = str(so)
ket_qua = ""
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0
while i < len(chuoi_so):
    ket_qua += chu_so[int(chuoi_so[i])] + " "
    i += 1

print(f"{so} doc la:", ket_qua.strip())

# input  Nhap vao so thap phan: 397
# output  397 doc la: ba chín bảy