def toiUu(s):
    s1 = s
    s1 = s1.strip()
    arr = s1.split(' ')
    s1 = ''
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            s1 = s1+word+' '
    return s1.strip()

s = '   tran  duy     hung  '

print(s, '=>', len(s))

s = toiUu(s)

print(s, '=>', len(s))