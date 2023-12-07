# Viết chương trình nhập vào điểm 3 môn Toán, Lý, Hóa của 1 học sinh. In ra điểm trung
#bình của học sinh đó với 2 số lẻ thập phân.

t = float(input('Nhập điểm môn Toán: '))
l = float(input('Nhập điểm môn Lý: '))
h = float(input('Nhập điểm môn Hóa: '))
dtb = (t + l + h) / 3

print('Điểm trung bình của 3 môn là: ', round(dtb, 2))
