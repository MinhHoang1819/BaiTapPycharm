a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
b[2] = 35

print('a[2] =', a[2])

b = a
b[2] = 113

print('a[2] =', a[2])

a[2] = 115

print('b[2] =', b[2])

c = b
c[3] = 999

print('a[3] =', a[3], ',', 'b[3] =', b[3])