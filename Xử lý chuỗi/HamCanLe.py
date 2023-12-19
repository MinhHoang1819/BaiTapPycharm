# Căn phải

word = 'ABCD'

print(word.rjust(10, '*'))
print(word.rjust(3, '*'))
print(word.rjust(15, '>'))
print(word.rjust(10))
print()

# Căn trái

word1 = 'OBAMA'

print(word1.ljust(1))
print(word1.ljust(2))
print(word1.ljust(3))
print(word1.ljust(4))
print(word1.ljust(5))
print(word1.ljust(10))
print(word1.ljust(10, '*'))
print()

# Căn giữa

word2 = 'TRUMP'
print(word2.center(10))
print(word2.center(10, '*'))
print(word2.center(21, '*'))