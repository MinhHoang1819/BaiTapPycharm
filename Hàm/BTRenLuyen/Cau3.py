def tong(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = int(input('Nhập n: '))

print('Tổng của các ước số:', tong(n))