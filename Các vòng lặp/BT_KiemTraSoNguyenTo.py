# Viết chương trình nhập vào 1 số, kiểm tra xem số này có phải là số nguyên tố hay
# không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.

while True:
    n = int(input('Nhập n: '))
    dem = 0
    for i in range(1, n+1):
        if n % 2 == 0:
            dem += 1
    if dem == 2:
        print(n, 'là số nguyên tố')
    else:
        print(n, 'không phải là số nguyên tố')
    hoi = input('Tiếp tục?(Y/N): ')
    if hoi is 'N':
        break
print('Tạm biệt!')