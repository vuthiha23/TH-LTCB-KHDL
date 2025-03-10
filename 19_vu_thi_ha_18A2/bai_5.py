print("nhap cac so nguyen,nhap so am de ket thuc chuong trinh!")
while True:
    try:
        so = int(input("nhap so nguyen:"))
        if so < 0:
            print("day la so am,chuong trinh ket thuc!")
            break
    except :
        print("vui long nhap mot so nguyen !")
  
  
# nhap cac so nguyen,nhap so am de ket thuc chuong trinh!
# nhap so nguyen:3
# nhap so nguyen:4
# nhap so nguyen:2
# nhap so nguyen:-1
# day la so am,chuong trinh ket thuc!      