#Dao DS
lst = [1, 2, 3, 4]

print(lst)

# lst.reverse()
#
# print(lst)

for i in range(len(lst)-1, -1, -1):
    print(lst[i], end='\t')

print()
print('*'*20)
lst = [8, 0, 2, 100, 20]

print(lst)

lst1 = reversed(lst)
for item in lst1:
    print(item)

print(lst)

lst = ['Obama', 'hahaha', 'ali33']

print(lst)

lst.reverse()

print(lst)