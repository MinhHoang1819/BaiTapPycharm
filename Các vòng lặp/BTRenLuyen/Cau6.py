# Vẽ hình vuông

n = int(input('Nhập n: '))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Vẽ hình tam giác

n1 = int(input('Nhập n1: '))
for i in range(n1):
    for j in range(n1):
        if j == n1-1 or i == n1-1 or (i == 2 and j == 1) or (j == 2 and i == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Vẽ 2 hình tam giác

n2 = int(input('Nhập n2: '))
for i in range(n2):
    for j in range(n2):
        if i == j or (j == 0 and i == 1) or (j == 0 and i == 2) or i == 3 or (j == n2-1 and i == n2-2) or (j == n2-1 and i == n2-3):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()