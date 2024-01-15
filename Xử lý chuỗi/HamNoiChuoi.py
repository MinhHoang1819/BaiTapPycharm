s = 'sv007;Nguyen Thi Tet;1/1/1990'
arr = s.split(';')

print(len(arr))

for x in arr:
    print(x)

s1 = ', '
s2 = s1.join(arr)

print(s2)