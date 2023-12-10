# s = 1 + 2 + 3 ... + n

n = int(input('Nhập n: '))
s = 0
i = 1
while i <= n:
    s = s + i
    i = i + 1
print('Tổng =', s)