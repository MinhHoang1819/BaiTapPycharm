# Vẽ hình vuông

# n = int(input('Nhập n: '))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# Vẽ hình tam giác

n = int(input('Nhập n: '))
for i in range(n):
    for j in range(n):
        if j == n-1 or i == n-1 or (i == 2 and j == 1) or (j == 2 and i == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()