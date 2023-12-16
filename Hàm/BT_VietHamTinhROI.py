# ROI = (Doanh thu - Chi phí) / Chi phí

def ROI(dt, cp):
    return (dt-cp) / cp

def goiYDauTu(roi):
    if roi >= 0.75:
        return 'Nên đầu tư'
    else:
        return 'Ko nên đầu tư'

print('Chương trình tính ROI')

dt = int(input('Nhập doanh thu: '))
cp = int(input('Nhập chi phí: '))
roi = ROI(dt, cp)

print('Tỉ lệ ROI:', roi)
print('=>', goiYDauTu(roi))
