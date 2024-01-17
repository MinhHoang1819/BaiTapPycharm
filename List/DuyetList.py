n = int(input('Nhap n: '))
lst = [0]*n
for i in range(n):
    lst[i] = randrange(-100, 100)

print(lst)
print('Duyet theo Collection: ')

for x in lst:
    print(x, end='\t')

print('\nDuyet theo Index: ')
for i in range(len(lst)):
    print('Vi tri', i, 'co gia tri:', lst[i])

print('Duyet nguoc DS: ')
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end='\t')