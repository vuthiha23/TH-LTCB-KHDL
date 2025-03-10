so_chu = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]

while True:
    try:
        n = int(input("nhap mot so nguyen:"))
        break
    except:
        print("vui long nhap mot so nguyen!")
        
if n < 0:
    ket_qua = "am"
    n = abs(n)
else:
    ket_qua = ""
    
for chu_so in str(n):
    ket_qua += so_chu[int(chu_so)] + " "
    
print(f"so {n} duoc doc la : {ket_qua.strip()}")

# nhap mot so nguyen:234
# so 234 duoc doc la : hai ba bo