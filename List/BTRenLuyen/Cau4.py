num = []
n = int(input('Nhap n: '))
for i in range(n):
    try:
        x = int(input(f'Nhap so thu {i+1}: '))
    except ValueError:
        print('Vui long nhap lai.')
        continue

    num.append(x)

num.sort()

print('Day so sau khi nhap: ', end='')

for x in num:
    print(x, end=' ')

print()
