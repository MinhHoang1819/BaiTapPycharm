def LuuFile(path):
    file = open(path, 'w', encoding='utf-8')
    file.writelines('SV01; Trần Thị Tẹt; 1/1/1998\n')
    file.writelines('SV02; Hồ Thị Tủn; 2/2/1997\n')
    file.writelines('SV03; Phạm Thị Thẹo; 3/3/1999\n')
    file.close()

LuuFile('DSSV.txt')