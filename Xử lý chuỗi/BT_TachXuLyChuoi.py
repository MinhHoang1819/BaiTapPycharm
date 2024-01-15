#Cau2
s = input('Nhap chuoi: ')
in_hoa = 0
in_thuong = 0
chu_so = 0
ky_tu = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0
nguyen_am_tap = set('aeiouAEIOU')
for str in s:
    if str.isupper():
        in_hoa += 1
    elif str.islower():
        in_thuong += 1
    elif str.isdigit():
        chu_so += 1
    elif str == ' ':
        khoang_trang += 1
    else:
        ky_tu += 1

    if str in nguyen_am_tap:
        nguyen_am += 1
    elif str.isalpha():
        phu_am += 1


print("Số ký tự in hoa:", in_hoa)
print("Số ký tự in thường:", in_thuong)
print("Số ký tự là chữ số:", chu_so)
print("Số ký tự là ký tự đặc biệt:", ky_tu)
print("Số ký tự là khoảng trắng:", khoang_trang)
print("Số ký tự là nguyên âm:", nguyen_am)
print("Số ký tự là phụ âm:", phu_am)

#Cau3