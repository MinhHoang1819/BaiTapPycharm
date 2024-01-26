from BT_XuLyFile import *

MaSP = input('Nhap ma san pham: ')
TenSP = input('Nhap ten san pham: ')
DonGia = float(input('Nhap don gia: '))
line = MaSP + "; " + TenSP + "; " + str(DonGia)

LuuFile('database.txt', line)