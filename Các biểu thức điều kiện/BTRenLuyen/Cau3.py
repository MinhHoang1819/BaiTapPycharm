so = {0: 'không', 1: 'một', 2: 'hai',
      3: 'ba', 4: 'bốn', 5: 'năm',
      6: 'sáu', 7: 'bảy', 8: 'tám',
      9: 'chín', 10: 'mười', 11: 'mười một',
      12: 'mười hai', 13: 'mười ba', 14: 'mười bốn',
      15: 'mười lăm', 16: 'mười sáu', 17: 'mười bảy',
      18: 'mười tám', 19: 'mười chín', 20: 'hai mươi',
      30: 'ba mươi', 40: 'bốn mươi', 50: 'năm mươi',
      60: 'sáu mươi', 70: 'bảy mươi', 80: 'tám mươi',
      90: 'chín mươi'}
def chu(n):
    if n in so:
        return so[n]
    else:
        chuc = n // 10
        donvi = n % 10
        if donvi == 0:
            return so[chuc*10]
        elif donvi == 1:
            return so[chuc*10] + ' mốt'
        elif donvi == 5:
            return so[chuc*10] + ' lăm'
        else:
            return so[chuc*10] + ' ' + so[donvi]
n = int(input('Nhập n: '))
if n < 0 or n > 99:
    print('Số không hợp lệ!')
else:
    print('n =', n, '==>', chu(n))