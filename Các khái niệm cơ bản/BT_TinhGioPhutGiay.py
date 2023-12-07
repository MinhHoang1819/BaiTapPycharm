# Nhập vào số giây bất kỳ t. Tính và xuất ra dạng h:m:s

t = int(input('Nhập t(s): '))
h = (t // 3600) % 24
m = (t % 3600) // 60
s = (t % 3600) % 60

print(h, ':', m, ':', s)