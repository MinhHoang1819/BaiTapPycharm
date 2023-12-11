n = 15
s = 0
for x in range(1, n + 1, 2):
    if x is 3 or x is 11:
        continue
    s = s + x
print('s =', s)