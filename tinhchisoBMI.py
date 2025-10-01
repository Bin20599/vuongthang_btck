can_nang=int(input("nhap can nang cua ban: "))
chieu_cao=int(input("nhap chieu cao cua ban: "))
BMI=can_nang/(chieu_cao**2)
if BMI<=18.5:
    print("thieu can!")
elif 18.5 <=BMI<=24.9:
    print("binh thuong")
elif 24.9<=BMI<=29.9:
    print("thua can!!")
else:
    print("beo phi")
    
