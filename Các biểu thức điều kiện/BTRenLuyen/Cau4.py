ngay = int(input('Nhập ngày: '))
thang = int(input('Nhập tháng: '))
nam = int(input('Nhập năm: '))
if ngay < 1 or ngay > 31 or thang < 1 and thang > 12 or nam < 1:
    print('Ngày, Tháng, Năm không hợp lệ!')
else:
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        songay = 31
    elif thang in [4, 6, 9, 11]:
        songay = 30
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
            songay = 29
        else:
            songay = 28
    if ngay < songay:
        ngay += 1
    else:
        ngay = 1
        if thang < 12:
            thang += 1
        else:
            thang = 1
            nam += 1
print('Ngày kế sau là:', ngay, '/', thang, '/', nam)
