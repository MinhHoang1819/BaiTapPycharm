from BT_DuLieuChuoiSo import *

arrSo = Read('csdl_so.txt')

print(arrSo)

def InSoAm(arrSo):
    for row in arrSo:
        for element in row:
            num = int(element)
            if num < 0:
                print(num, end='\t')

        print()

print('Cac so am tren moi dong: ')

InSoAm(arrSo)