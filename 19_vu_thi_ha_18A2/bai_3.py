import math

x = float(input("Nhập x: "))

cos_x = 1
tử_số = -x**2
mẫu_số = 2
giá_trị_hạng = tử_số / mẫu_số

while abs(giá_trị_hạng) > 1e-4:
    cos_x += giá_trị_hạng
    tử_số *= -x**2
    mẫu_số *= (mẫu_số + 1) * (mẫu_số + 2)
    giá_trị_hạng = tử_số / mẫu_số

print(f"cos({x}) ≈ {cos_x}")

# Nhập x: 0.5
# cos(0.5) ≈ 0.8776041666666666
