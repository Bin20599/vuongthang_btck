year=int(input("nhap mot nam:"))
if(year%4==0 and year%100!=0)or(year%400==0):
    print("nam",year,"la nam nhuan.")
else:
    print("nam",year,"khong phai la nam nhuan.")