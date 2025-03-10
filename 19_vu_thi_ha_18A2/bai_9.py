while True:
    try:
        n = int(input("nhap mot so nguyen:"))
        break
    except:
        print("vui long nhap mot so nguyen!")
n = abs(n)
tong = sum(int(chu_so) for chu_so in str(n))

print(f"tong cac chu so cua {n} la : {tong}")

# intput     nhap mot so nguyen:234
# output     tong cac chu so cua 234 la : 9