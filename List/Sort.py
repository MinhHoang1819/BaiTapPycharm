#Sap xep
from random import randrange

lst = [0]*10
for i in range(len(lst)):
    lst[i] = randrange(100)

print(lst)

lst.sort()

print(lst)
print('*'*20)

lst = [4, 2, 10, 8]
ls1 = sorted(lst)

print(lst)
print(ls1)
print('#'*20)

lst = [8, 2, 10, 3]
lst.sort(reverse=True)

print(lst)