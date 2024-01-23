from random import randrange

def soNguyenTo(n):
    d = 0
    for i in range(1, n+1):
        if (n%i == 0):
            d += 1

    return d == 2

M = []
n = int(input('Nhap n: '))
for i in range(n):
    M.append(randrange(0, 100))

print('Mang ngau nhien: ')
print(M)

so_le = []
so_chan = []
so_ngto = []
so_khong_ngto = []
for x in M:
    if x%2 == 1:
        so_le.append(x)
    else:
        so_chan.append(x)

    if soNguyenTo(x):
        so_ngto.append(x)
    else:
        so_khong_ngto.append(x)

so_le.sort()
so_chan.sort()
so_ngto.sort()
so_khong_ngto.sort()


print("Dòng 1: gồm các số lẻ, tổng cộng có", len(so_le), "số lẻ.")
for x in so_le:
    print(x, end=" ")

print()

print("Dòng 2: gồm các số chẵn, tổng cộng có", len(so_chan), "số chẵn.")

for x in so_chan:
    print(x, end=" ")

print()

print("Dòng 3: gồm các số nguyên tố.")

for x in so_ngto:
    print(x, end=" ")

print()

print("Dòng 4: gồm các số không phải là số nguyên tố.")

for x in so_khong_ngto:
    print(x, end=" ")

print()