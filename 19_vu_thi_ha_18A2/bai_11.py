
print("Menu do uong:")
print("1. Cafe")
print("2. Cam vat")
print("3. Nuoc ep ca rot")
print("4. Nuoc loc")
print("5. Nuoc dua")
chon = 0
while chon < 1 or chon > 5:
    chon = int(input("Nhap lua chon cua ban: "))
    if chon < 1 or chon > 5:
        print("Vui long chon so tu 1 den 5!")
if chon == 1:
    print("Ban da chon Cafe.")
elif chon == 2:
    print("Ban da chon cam vat.")
elif chon == 3:
    print("Ban da chon nuoc ep ca rot.")
elif chon == 4:
    print("Ban da chon nuoc loc.")
elif chon == 5:
    print("Ban da chon nuoc loc.")
    
# Menu do uong:
# 1. Cafe
# 2. Cam vat
# 3. Nuoc ep ca rot
# 4. Nuoc loc
# 5. Nuoc dua
# intput    Nhap lua chon cua ban: 1
# output    Ban da chon Cafe.