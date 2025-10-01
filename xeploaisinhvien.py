toan=float(input("diem toan: "))
van=float(input("diem van: "))
anh=float(input("diem anh: "))
total=toan+van+anh
average=total/3
print("diem trung binh cua sinh vien: ",average)
if average>=8.5:
    print("xep loai hoc luc: gioi")
elif average<8.5:
    print("xep loai hoc luc: kha!")
elif average<7.0:
    print("xep loai hoc luc: trung binh")
else:
    print("xep loai hoc luc: yeu!!")