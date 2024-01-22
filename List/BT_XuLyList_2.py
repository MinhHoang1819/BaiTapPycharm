from random import randrange

lst = []
n = int(input('Nhap n: '))
for i in range(n):
    lst.append(randrange(0, 100))

print('List ngau nhien: ')
print(lst)

k = int(input('Nhap k: '))
while lst.count(k) > 0:
    lst.remove(k)

print('List sau khi xoa: ')
print(lst)

def doiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-i-1]:
            return False

    return True

kt = doiXung(lst)
if kt == True:
    print('List doi xung.')
else:
    print('List khong doi xung.')