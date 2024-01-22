from random import randrange


def Matrix(m, n):
    d = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))

        d.append(row)
    return d

def xuatMatrix(d):
    for row in d:
        for element in row:
            print(element, end='\t')

        print()

def layDong(r):
    r = d[r]
    return d

def xuatList1Chieu(r):
    for element in r:
        print(element, end='\t')

def layCot(c):
    C = []
    for i in range(len(d)):
        C.append(d[i][c])

    return C

def max(d):
    max = d[0][0]
    for i in range(len(d)):
        for j in range(len(d[i])):
            if (max < d[i][j]):
                max = d[i][j]

    return max

m = int(input('Nhap so dong: '))
n = int(input('Nhap so cot: '))
d = Matrix(m, n)

print(d)

xuatMatrix(d)
r = int(input('Nhap dong can xuat: '))
xuatList1Chieu(layDong(r))

print()

c = int(input('Nhap cot can lay: '))
xuatList1Chieu(layCot(c))

print()

max = max(d)

print('So lon nhat trong ma tran:', max)