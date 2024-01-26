from BT_XuLyFile import *

DS = Read('database.txt')

#print(DS)

def InSP(DS):
    for row in DS:
        for element in row:
            print(element, end='\t')

        print()

    print()

InSP(DS)

def Sort(DS):
    for i in range(len(DS)):
        for j in range(len(DS)):
            a = DS[i]
            b = DS[j]
            if a[2] > b[2]:
                DS[i] = b
                DS[j] = a

Sort(DS)

print('San pham sau khi sap xep: ')

InSP(DS)