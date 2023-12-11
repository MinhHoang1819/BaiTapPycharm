while True:
    x = int(input('Nhập x: '))
    print(x, 'là số chẵn' if x % 2 == 0 else 'là số lẻ')
    hoi = input('Tiếp tục?(Y/N): ')
    if  hoi == 'N':
        break;
print('Tạm biệt!')
