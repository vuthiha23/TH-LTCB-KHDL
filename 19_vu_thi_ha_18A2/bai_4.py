tu_so = int(input("nhap tu so:"))
while True:
    mau_so = int(input("nhap mau so:"))
    if mau_so != 0:
        break
    print("mau so khong duoc bang 0,yeu cau nhap lai!")
phan_so = tu_so/mau_so
print(f"phan so co gia tri la: {tu_so}/{mau_so}")
#    nhap tu so:3
#    nhap mau so:0
#    mau so khong duoc bang 0,yeu cau nhap lai!
#    nhap mau so:4
#    phan so co gia tri la: 3/4