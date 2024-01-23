import numpy as np

def Matrix():
    m = int(input('Nhap so dong: '))
    n = int(input('Nhap so cot: '))
    M = np.empty((m, n))
    for i in range(m):
        row = []
        for j in range(n):
           M[i][j] = float(input(f'Nhap phan tu o hang {i+1}, cot {i+1}: '))

    return M

def SumMatrix(M1, M2):
    if M1.shape == M2.shape:
        sum = M1 + M2
        return sum

def HoanVi_Hang(M, m1, m2):
    if (0 <= m1 < M.shape[0] and 0 <= m2 < M.shape[0]):
        temp = M[m1].copy()
        M[m1] = M[m2]
        M[m2] = temp
        return M

def HoanVi_Cot(M, n1, n2):
    if (0 <= n1 < M.shape[1] and 0 <= n2 < M.shape[1]):
        temp = M[:, n1].copy()
        M[:, n1] = M[:, n2]
        M[:, n2] = temp
        return M

print("Nhập ma trận A:")

A = Matrix()

print("Ma trận A là:")
print(A)
print("Nhập ma trận B:")

B = Matrix()

print("Ma trận B là:")
print(B)

C = SumMatrix(A, B)

print('Tong cua A va B la: ')
print(C)
print('Hoan vi hai hang cua ma tran A la: ')

m1 = int(input('Nhap hang thu nhat: '))
m2 = int(input('Nhap hang thu hai: '))
A = HoanVi_Hang(A, m1, m2)

print("Ma trận A sau khi hoán vị hai hàng là:")
print(A)
print('Hoan vi hai hang cua ma tran B la: ')

n1 = int(input('Nhap hang thu nhat: '))
n2 = int(input('Nhap hang thu hai: '))
B = HoanVi_Cot(B, n1, n2)

print("Ma trận B sau khi hoán vị hai hàng là:")
print(B)