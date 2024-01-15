s = 'sv007;Nguyen Thi Tet;1/1/1990'
arr = s.split(';')

print(len(arr))

for x in arr:
    print(x)

s1 = """
Obama
hahaha
ali333
"""
arr1 = s1.splitlines()
for line in arr:
    print(line, 'a->', line.count('a'))

s2 = """
sv01;Nguyen Thi Hanh;1/1/1990
sv02;Tran Van Phuc;2/2/1995
sv03;Ho Van An;2/3/1998
sv04;Pham Thi Lanh;4/4/1994
"""
arrSV = s2.splitlines()
for line1 in arrSV:
    arrInFor = line1.strip().split(';')
    if len(arrInFor) == 3:
        print(arrInFor)