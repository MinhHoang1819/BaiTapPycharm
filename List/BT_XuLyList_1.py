from random import randrange

n = int(input('Nhap n: '))
lst = [0]*n
for i in range(n):
    lst[i] = randrange(-100, 100)

print('List ngau nhien la: ')
print(lst)
print('Them phan tu vao list: ')

value = int(input('Nhap phan tu: '))
lst.append(value)

print(lst)
print('Dem phan tu trong list: ')

k = int(input('Nhap k: '))
dem = lst.count(k)

print(k, 'xuat hien', dem, 'lan trong list.')

def soNguyenTo(n):
    d = 0
    for i in range(1, n+1):
        if (n%i == 0):
            d += 1

    return d == 2

demnt = 0
tongnt = 0
for x in lst:
    if soNguyenTo(x):
        demnt += 1
        tongnt += x

print('Co', demnt, 'so nguyen to trong list.')
print('Tong =', tongnt)

lst.sort()
print('Sap xep list: ')
print(lst)

del lst
print('Xoa list: ')
print(lst)