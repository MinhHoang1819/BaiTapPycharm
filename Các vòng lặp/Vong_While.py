print('Nhập 1 số [1..10]')
x = -1
while x < 1 or x > 10:
    x = int(input('Nhập số: '))
print(x**2)