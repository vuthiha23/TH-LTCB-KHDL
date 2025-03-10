import math
n = int(input("nhap so nguyen n : "))
while n <= 0 :
    n = int(input("Nhap lai so nguyen dương n la : "))
s1 = 0 
dau = 1 
i = 1 
while i <= n :
    s1 = s1 + (dau * (1/i))
    dau = -dau 
    i = i + 1 
print(f"gia tri cau a la {s1}")
s2 = 0 
i = 1
while i <= n :
    s2 = s2 + (1/(i *(i +1)) )
    i = i + 1 
print(f"gia tri cau b la {s2}")
s3 = 0 
i = 2 
while i <= n : 
    s3 = s3 +  1 / (math.sqrt(i))
    i = i + 1 
print(f"gia tri cau c la {s3}")
#input    nhap so nguyen n : 4
#output    gia tri cau a la 0.5833333333333333
#          gia tri cau b la 0.8
#          gia tri cau c la 1.7844570503761732