def FN(n, m=0):
    s = 0
    for i in range(1, m+n, 1):
        s += i
    return s

print(FN(5))
print(FN(5, 1))
print('*'*30)

def FN2(n, m=1, k=2):
    s = 0
    for i in range(1, m+n+k, 1):
        s += i
    return s

print(FN2(5))
print(FN2(5, 3))        #1+2+3+4+5+6+7+8+9
print(FN2(5, 3, 1))  #1+2+3+4+5+6+7+8
print(FN2(5, k=4))
print('*'*30)

lst = ['obama', 'putin', 'kim jong un']
for item in lst:
    print(item, end='\t')