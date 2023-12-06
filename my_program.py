#Cau 1
s = arange('pYthoN')
print(s)

#Cau 2
s1 = 'Abc'
s2 = 'Xyz'
s3 = mix(s1, s2)
print(s3)

#Cau 3
s1 = 'Dai hoc Khoa hoc'
s2 = 'Khoa hoc'
s3 = count_occurences(s1, s2)
print(s3)

#Cau 4
s = 'Thu 6 ngay 3'
x = sum_average(s)
print(x)

#Cau 5
s = last_position("hello world", "l")
print(s)

#Cau 6
L1 = ["H", "na", "i", "H", '18 years old']
L2 = ["is", "me", "s", "ao"]
L3 = concatenate(L1, L2)
print(L3)

#Cau 7
L = [1, 2, [30, 40, [500, 600], 50], 3, 4]
item = 600, new_item = 800
s = add_new(L, item, new_item)
print(s)

#Cau 8
M1 = [[1, 0, 0], [1, 1, 0]]
M2 = [[1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
M3 = multiply_matrix(M1, M2)
print(M3)