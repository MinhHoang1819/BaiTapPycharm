#Cau 1
def arange(s):
    lower_chars = sorted([char for char in s if char.islower()])
    upper_chars = sorted([char for char in s if char.isupper()])
    return ''.join(lower_chars + upper_chars)

#Cau 2
def mix(s1, s2): 
    s3 = ''
    for i in range(min(len(s1), len(s2))):
        s3 += s1[i] + s2[i]
    if len(s1) > len(s2):
        s3 += s1[len(s2):]
    elif len(s1) < len(s2):
        s3 += s2[len(s1):]
    return s3

#Cau 3
def count_occurences(s1, s2):
    return s1.lower().count(s2.lower())

#Cau 4
def sum_average(s):
    digits = [int(char) for char in s if char.isdigit()]
    return sum(digits), sum(digits) / len(digits) if digits else 0

#Cau 5
def last_position(S1, S2):
    pos = S1.rfind(S2)
    return pos

#Cau 6
def concatenate(L1, L2):
    return [L1[i] + L2[i] for i in range(min(len(L1), len(L2)))]

#Cau 7
def add_new(L, item, new_item):
    index = L.index(item)
    return L[:index+1] + [new_item] + L[index+1:]

#Cau 8
def multiply_matrix(M1, M2):
    if len(M1[0]) != len(M2):
        return "Không thể nhân hai ma trận này."
    else:
        result = [[0 for j in range(len(M2[0]))] for i in range(len(M1))]
        for i in range(len(M1)):
            for j in range(len(M2[0])):
                for k in range(len(M2)):
                    result[i][j] += M1[i][k] * M2[k][j]
        return result
