def UCLN(a, b):
    """Hàm này dùng để tìm UCLN"""
    min = a if a < b else b
    for i in range(min, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

uoc = UCLN(25, 15)
print(uoc)