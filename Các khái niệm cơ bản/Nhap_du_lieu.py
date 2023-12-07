print('Nhập giá trị: ')
s = input()
print(s)
print(type(s))

def StrToBool(s):
    return s.lower() in ('true', 't', '1', 'yes')

x = input('Nhập giá trị: ')
x = StrToBool(x)
print(x)