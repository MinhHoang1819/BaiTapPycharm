from random import randrange

lst = []
n = int(input('Nhap n: '))
for i in range(n):
    lst.append(randrange(0, 100))

print('List ngau nhien: ')
print(lst)