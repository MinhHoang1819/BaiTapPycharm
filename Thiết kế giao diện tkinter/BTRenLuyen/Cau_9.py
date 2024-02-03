from tkinter import *

def Tinh():
    cn = float(can_nang.get())
    cc = float(chieu_cao.get())
    BMI = cn / (cc/100)**2
    bmi.set(f'{BMI:.2f}')
    if BMI < 18.5:
        tinh_trang.set(f'Bạn thiếu cân')
    elif BMI < 25:
        tinh_trang.set(f'Bạn cân đối')
    elif BMI < 30:
        tinh_trang.set(f'Bạn thừa cân')
    else:
        tinh_trang.set(f'Bạn béo phì')

root = Tk()
root.title('BMI')
root.resizable(height=True, width=True)
root.minsize(height=320, width=275)

can_nang = StringVar()
chieu_cao = StringVar()
bmi = StringVar()
tinh_trang = StringVar()

Label(root, text='Nhập chiều cao:').grid(row=0, column=0)
Entry(root, width=20, textvariable=chieu_cao).grid(row=0, column=1)

Label(root, text='Nhập cân nặng:').grid(row=1, column=0)
Entry(root, width=20, textvariable=can_nang).grid(row=1, column=1)

Button(root, text='Tính BMI', command=Tinh).grid(row=2, column=1)

Label(root, text='BMI của bạn:').grid(row=3, column=0)
Entry(root, width=20, textvariable=bmi).grid(row=3, column=1)

Label(root, text='Tình trạng của bạn:').grid(row=4, column=0)
Entry(root, width=20, textvariable=tinh_trang).grid(row=4, column=1)

Button(root, text='Thoát', command=root.quit).grid(row=5, column=1)

root.mainloop()