# BMI = cân nặng(kg) / chiều cao x chiều cao(m)

def BMI(height, weight):
    return weight / (height**2)

def phanLoai(bmi):
    if bmi < 18.5:
        return 'Gầy'
    elif bmi <= 24.9:
        return 'Bình thường'
    elif bmi <= 29.9:
        return 'Hơi béo'
    elif bmi <= 34.9:
        return 'Béo phì cấp độ 1'
    elif bmi <= 39.9:
        return 'Béo phì cấp độ 2'
    else:
        return 'Béo phì cấp độ 3'

def nguyCoBenh(bmi):
    if bmi < 18.5:
        return 'Thấp'
    elif bmi <= 24.9:
        return 'Trung bình'
    elif bmi <= 29.9:
        return 'Cao'
    elif bmi <= 34.9:
        return 'Cao'
    elif bmi <= 39.9:
        return 'Rất cao'
    else:
        return 'Nguy hiểm'

print('Nhập chiều cao: ')
height = float(input())

print('Nhập cân nặng: ')
weight = float(input())

bmi = BMI(height, weight)

print('BMI =', bmi)
print('Phân loại:', phanLoai(bmi))
print('Nguy cơ bệnh: ', nguyCoBenh(bmi))