s = 'C:/music/bolero/doithong2mo.mp3'
p1 = s.find('/')
p2 = s.rfind('/')

print('p1 =', p1)
print('p2 =', p2)

c = s.count('o')
print('o xuất hiện:', c)

c = s.count('o', 16)
print('o xuất hiện', c, 'từ vị trí thứ 16 của chuỗi gốc')

c = s.count('o', 16, 20)
print('o xuất hiện', c, 'từ vị trí thứ 16->20 của chuỗi gốc')