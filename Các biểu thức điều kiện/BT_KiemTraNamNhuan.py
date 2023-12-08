# Nhập vào 1 năm bất kì, kiểm tra năm đó có phải là năm nhuận hay không? Biết rằng:
# năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc không chia hết cho 400.

year = int(input('Nhập năm: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Năm', year, 'là năm nhuận')
else :
    print('Năm', year, 'không phải là năm nhuận')