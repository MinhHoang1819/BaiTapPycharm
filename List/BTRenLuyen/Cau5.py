M = []
n = int(input('Nhap n: '))
for i in range(n):
    try:
        x = int(input(f'Nhap so thu {i+1}: '))
    except ValueError:
        print('Vui long nhap lai.')
        continue

    M.append(x)

M.sort(reverse=True)

print('Day so sau khi nhap: ', end='')

for x in M:
    print(x, end=' ')

print()
