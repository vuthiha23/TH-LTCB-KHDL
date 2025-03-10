while True:
    try:
        n = int(input("nhap so nguyen duong n:"))
        if n > 0:
            break
        else:
            print("vui long nhap so nguyen duong!")
    except:
        print("nhap sai,yeu cau nhap so nguyen duong!")
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i**3
    i += 2
S6 = 0
i = 2
while i <= (2 * n):
    S6 += i**4
    i += 2
print(f"tong S4 = {S4}")
print(f"tong S5 = {S5}")
print(f"tong S6 = {S6}")
# input nhap so nguyen duong n:4
# output tong S4 = 30
#        tong S5 = 1225
#        tong S6 = 5664