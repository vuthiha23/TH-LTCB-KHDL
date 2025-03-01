# BAI 1
n = int(input("nhap nam tu ban phim cua ban: "))
if n % 4 == 0 and n % 100 != 0:
    print("nam nay la nam nhuan")
elif n % 400 == 0:
    print("nam nay la nam nhuan")
else:
    print("day khong phai la nam nhuan!")

# BAI 2
x = float(input("nhap toa do x:"))
y = float(input("nhap toa do y:"))
a = float(input("nhap toa do a:"))
b = float(input("nhap toa do b:"))
R = float(input("nhap ban kinh R:"))
IM = ((x-a)**2 + (y-b)**2)**(1/2)
print(f"do dai IM bang :{IM}")
if IM < R:
    print("M nam trong duong tron")
elif IM == R:
    print("M nam tren duong tron") 
else:
    print("M nam ngoai duong tron")   

# BAI 3
a = float(input("nhap do dai canh a:"))
b = float(input("nhap do dai canh b:"))
c = float(input("nhap do dai canh c:"))
if a + b <= c or a + c <= b or b + c <= a:
    print("khong phai la bo ba canh cua tam giac")
else:
    if a == b == c:
        print("tam giac deu")
    elif a == b or b == c or a == c:
        print("tam giac can")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("tam giac vuong")
    elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) and (a == b or b == c or a == c):
        print("tam giac vuong can")
    else:
        print("tam giac thuong")

# BAI 4
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c

# In kết quả
print(f"so lon nhat la:{so_lon_nhat}")     
 
# BAI 5
ky_tu = input("Nhập một ký tự: ").lower()  # Chuyển về chữ thường để dễ kiểm tra

# Danh sách các nguyên âm
nguyen_am = "aeiou"

# Kiểm tra xem có phải chữ cái không
if ky_tu.isalpha() and len(ky_tu) == 1:
    if ky_tu in nguyen_am:
        print(f"{ky_tu} là nguyên âm.")
    else:
        print(f"{ky_tu} là phụ âm.")
else:
    print("Vui lòng nhập một ký tự chữ cái hợp lệ!")

# BAI 6
def hien_thi_menu():
    print("\n🎬 Chào mừng đến với rạp chiếu phim ABC 🎬")
    print("Vui lòng chọn thể loại phim bạn muốn xem:")
    print("1. Hành động")
    print("2. Hài hước")
    print("3. Kinh dị")
    print("4. Khoa học viễn tưởng")
    print("5. Lãng mạn")
    print("6. Hoạt hình")
    print("0. Thoát")

# Chạy chương trình
while True:
    hien_thi_menu()
    
    try:
        lua_chon = int(input("Nhập số tương ứng với thể loại phim: "))

        if lua_chon == 1:
            print("Bạn đã chọn thể loại phim Hành động! ")
        elif lua_chon == 2:
            print("Bạn đã chọn thể loại phim Hài hước! ")
        elif lua_chon == 3:
            print("Bạn đã chọn thể loại phim Kinh dị! ")
        elif lua_chon == 4:
            print("Bạn đã chọn thể loại phim Khoa học viễn tưởng! ")
        elif lua_chon == 5:
            print("Bạn đã chọn thể loại phim Lãng mạn! ")
        elif lua_chon == 6:
            print("Bạn đã chọn thể loại phim Hoạt hình! ")
        elif lua_chon == 0:
            print("Cảm ơn bạn đã sử dụng dịch vụ. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    except :
        print("Vui lòng nhập một số hợp lệ từ 0 đến 6!")


# BAI 8
# Nhập điểm chữ từ người dùng
diem = input("Nhập điểm học tập (A, B, C, D, E, F): ").upper()

# Phân loại sinh viên theo điểm
if diem == "A":
    print("Sinh viên xuất sắc!")
elif diem == "B":
    print("Sinh viên loại giỏi!")
elif diem == "C":
    print("Sinh viên loại khá!")
elif diem == "D":
    print("Sinh viên loại trung bình!")
elif diem == "E":
    print("Sinh viên loại yếu!")
elif diem == "F":
    print("Sinh viên xếp loại kém!")
else:
    print("Điểm nhập không hợp lệ! Vui lòng nhập A, B, C, D, E hoặc F.")

# BAI 9
# Nhập lương từ người dùng
luong = float(input("Nhập lương nhân viên (triệu VND): "))

# Tính thuế thu nhập theo mức lương
if luong >= 15:
    thue = 0.30 * luong  # 30% thuế
elif 7 <= luong < 15:
    thue = 0.20 * luong  # 20% thuế
else:
    thue = 0.10 * luong  # 10% thuế

# Tính lương ròng
luong_rong = luong - thue

# Hiển thị kết quả
print(f"Thuế thu nhập: {thue:.2f} triệu VND")
print(f"Lương ròng (số tiền thực nhận): {luong_rong:.2f} triệu VND")

# BAI 10
def la_nam_nhuan(nam):
    """Hàm kiểm tra năm nhuận"""
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    """Hàm trả về số ngày trong tháng, có xét năm nhuận"""
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return None

# Nhập tháng và năm từ người dùng
try:
    thang = int(input("Nhập tháng (1-12): "))
    nam = int(input("Nhập năm: "))

    so_ngay = so_ngay_trong_thang(thang, nam)

    if so_ngay:
        print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
    else:
        print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")
except :
    print("Vui lòng nhập số nguyên hợp lệ cho tháng và năm!")

# BAI 11
def doc_so(n):
    """Hàm đọc số nguyên có ba chữ số"""
    hang_tram = ["", "Một trăm", "Hai trăm", "Ba trăm", "Bốn trăm", "Năm trăm",
                 "Sáu trăm", "Bảy trăm", "Tám trăm", "Chín trăm"]
    hang_chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi",
                 "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]
    hang_dv = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

    # Lấy từng chữ số hàng trăm, chục, đơn vị
    tram = n // 100
    chuc = (n % 100) // 10
    dv = n % 10

    # Xây dựng cách đọc
    doc_so_nguyen = hang_tram[tram]

    if chuc == 0:
        if dv == 0:
            doc_so_nguyen 
        else:
            doc_so_nguyen += " lẻ " + hang_dv[dv]
    elif chuc == 1:
        if dv == 0:
            doc_so_nguyen += " mười"
        elif dv == 5:
            doc_so_nguyen += " mười lăm"
        else:
            doc_so_nguyen += " mười " + hang_dv[dv]
    else:
        doc_so_nguyen += " " + hang_chuc[chuc]
        if dv == 0:
            doc_so_nguyen += hang_chuc[chuc] 
        elif dv == 5:
            doc_so_nguyen += " lăm"
        else:
            doc_so_nguyen += " " + hang_dv[dv]

    return doc_so_nguyen.strip()

# Nhập số từ người dùng
try:
    so = int(input("Nhập số nguyên có 3 chữ số (100-999): "))

    if 100 <= so <= 999:
        print(f"Cách đọc: {doc_so(so)}")
    else:
        print("Vui lòng nhập số có đúng 3 chữ số từ 100 đến 999!")
except:
    print("Vui lòng nhập một số nguyên hợp lệ!")

# BAI 12
LUONG_CO_BAN = 1350000  

def tinh_luong(tnct):
    """Hàm tính lương dựa trên thâm niên công tác"""
    if tnct < 12:
        he_so = 2.34
    elif 12 <= tnct < 36:
        he_so = 3.33
    elif 36 <= tnct < 60:
        he_so = 3.66
    else:  # TNCT >= 60 tháng
        he_so = 3.99
    
    luong = he_so * LUONG_CO_BAN
    return he_so, luong

# Nhập thâm niên công tác từ người dùng
try:
    tnct = int(input("Nhập số tháng làm việc của nhân viên: "))

    if tnct < 0:
        print("Thâm niên công tác không thể là số âm!")
    else:
        he_so, luong = tinh_luong(tnct)
        print(f"Hệ số lương: {he_so}")
        print(f"Lương của nhân viên: {luong} đồng")  # Hiển thị có dấu phẩy phân tách
except :
    print("Vui lòng nhập một số nguyên hợp lệ!")
