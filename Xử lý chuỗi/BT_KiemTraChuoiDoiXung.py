def kiemTra(s):
    flag = True
    for i in range(len(s)):
        if s[i] == s[len(s)-i-1]:
            flag = False

def main():
    print('Nhap 1 chuoi: ')
    s = input()
    if (kiemTra(s)):
        print('Chuoi bn nhap doi xung!')
    else:
        print('Chuoi bn nhap ko doi xung!')

while True:
    main()
    print('Tiep tuc?')
    s = input()
    if s == 'k':
        break

print('Cam on!')