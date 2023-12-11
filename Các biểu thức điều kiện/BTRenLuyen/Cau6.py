thang = int(input('Nhập tháng: '))
if thang < 1 or thang > 12:
    print('Tháng không hợp lệ!')
else:
    if thang in [1, 2, 3]:
        quy = 1
    elif thang in [4, 5, 6]:
        quy = 2
    elif thang in [7, 8, 9]:
        quy = 3
    else:
        quy = 4

    print('Tháng', thang, 'thuộc quý', quy, 'trong năm.')