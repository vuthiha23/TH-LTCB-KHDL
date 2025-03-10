import math
def bcnn(a,b):
    return abs(a*b)//math.gcd(a,b)

while True:
    try:
        a = int(input("nhap so nguyen duong thu nhat:"))
        b = int(input("nhap so nguyen duong thu hai:"))
        if a > 0 and b > 0:
            break
        else:
            print("vui long nhap hai so nguyen duong!")
    except:
        print("vui long nhap so nguyen hop le!")
        
ket_qua = bcnn(a,b)
print(f"boi chung nho nhat cua {a} va {b} la {ket_qua}")

#nhap so nguyen duong thu nhat:3
#nhap so nguyen duong thu hai:5
#boi chung nho nhat cua 3 va 5 la 15