from random import randrange

lst = [
    [100, 14, 8, 22, 71],
    [0, 243, 68, 1, 30],
    [90, 21, 7, 67, 112],
    [115, 200, 70, 150, 8]
]

print(lst)

for row in lst:  #Duyet tung dong
    for column in row:    #Lay tung phan tu tren moi dong
        print(column, end='\t')

    print()

print('*'*20)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end='\t')

    print()

arr2D = []
rowsize = int(input('Nhap so dong: '))
columnsize = int(input('Nhap so cot: '))
for i in range(rowsize):
    onerow = []
    for j in range(columnsize):
        onerow.append(randrange(-100, 100))

    arr2D.append(onerow)

print('Ma tran: ')
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j], end='\t')

    print()