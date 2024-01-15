s = "D:/tailieu/python/lamcchupython.pdf"
p = s.rfind('/')

print(s[p+1:])

p2 = s.rfind('.')

print(s[p+1:p2])
#format

a = 5
b = 9
c = a/b
s = '{0} / {1} = {2}'.format(a, b, c)

print(s)
