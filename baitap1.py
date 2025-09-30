cart=[]
while True:
    print("="*10,"MENU GIO HANG","="*10)
    print("1.Them san pham")
    print("2.Xoa san pham")
    print("3.Xem gio hang")
    print("4.Thoat")
    chon=input("chon chuc nang:")
    if chon=="1":
        product=input("nhap ten san pham: ")
        cart.append(product)
        print(f"da them'{product}'vao gio hang cua ban")
    elif chon=="2":
        product=input("nhap ten san pham muon xoa: ")
        cart.remove(product)
        print(f"san pham'{product}'da duoc xoa!")
    elif chon=="3":
        print("gio hang cua ban: ",cart)
    elif chon=="4":
        print("thoat chuong trinh.")
        print("tong so luong san pham trong gio hang cua ban:",len(cart))
        break