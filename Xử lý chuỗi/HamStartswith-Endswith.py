s = '#Hello Python*'

print(s.startswith('#'))
print(s.startswith('*'))
print(s.endswith('#'))
print(s.endswith('*'))

s1 = 'C:/music/bolero/longme.mp4'
if s.endswith('.mp3'):
    print('Bài hát này định dạng mp3')
else:
    print('Bài hát này không định dạng mp3')

s2 = '***OBAMA###'
print(s2.startswith('$'))

def LocSoDT(dauso):
    dssArr = ['0784329454', '0923465874', '0843245943', '0238509235', '0293443253']
    for phone in dssArr:
        if (phone.startswith(dauso)):
            return phone;
    return '<empty>';

print('Nhập đầu số:')
dauso = input()
phone = LocSoDT(dauso)

print(phone)

def LocToanBoSoPhone(dauso1):
    dssArr1 = ['0784329454', '0923465874', '0843245943', '0238509235', '0293443253']
    dsFound = []
    for phone1 in dssArr1:
        if(phone1.startswith(dauso1)):
            dsFound.append(phone1)
    return dsFound

dauso1 = input('Nhập đầu số: ')
dsFound = LocToanBoSoPhone(dauso1)

print(dsFound)
