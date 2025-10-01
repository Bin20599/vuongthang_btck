print("=== Chuyển đổi nhiệt độ ===")
print("1. Celsius (°C) ➡ Fahrenheit (°F)")
print("2. Fahrenheit (°F) ➡ Celsius (°C)")
chon=input("lua chon phuong thuc chuyen doi:")
if chon=="1":
    c=float(input("nhap nhiet do c:"))
    f=(c*9/5)+32
    print(f"Nhiệt độ {c}°C tương đương {f:.2f}°F.")
    if c>35:
        print("thoi tiet rat nong 🥵")
    elif c>25:
        print("thoi tiet mat me")
    elif c>=20:
        print("thoi tiet hoi xe lanh")
    else :
        print("thoi tiet rat lanh")

elif chon=="2":
    f=float(input("nhap nhiet do f:"))
    c=(f-32)*5/9
    print(f"Nhiệt độ {f}°F tương đương {c:.2f}°C.")
    if c>35:
        print("thoi tiet rat nong")
    elif c>25:
        print("thoi tiet mat me")
    elif c>=20:
        print("thoi tiet hoi xe lanh")
    else:
        print("thoi tiet rat lanh")
else:
    print("lua chon khong phu hop")   
