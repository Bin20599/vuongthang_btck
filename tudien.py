
dictionary = {}

def them_tu():
    word = input("Nhập từ mới: ").strip().lower()
    if word in dictionary:
        print(f"Từ '{word}' đã có trong từ điển.")
    else:
        meaning = input("Nhập nghĩa của từ: ").strip()
        dictionary[word] = meaning
        print(f" Đã thêm '{word}' vào từ điển.")

def xoa_tu():
    word = input("Nhập từ cần xóa: ").strip().lower()
    if word in dictionary:
        del dictionary[word]
        print(f" Đã xóa '{word}' khỏi từ điển.")
    else:
        print(f" Từ '{word}' không có trong từ điển.")

def cap_nhat_nghia():
    word = input("Nhập từ cần cập nhật: ").strip().lower()
    if word in dictionary:
        new_meaning = input("Nhập nghĩa mới: ").strip()
        dictionary[word] = new_meaning
        print(f" Đã cập nhật nghĩa của '{word}'.")
    else:
        print(f" Từ '{word}' chưa có trong từ điển.")

def tra_cuu():
    word = input("Nhập từ cần tra cứu: ").strip().lower()
    if word in dictionary:
        print(f" Nghĩa của '{word}': {dictionary[word]}")
    else:
        print(f" Từ '{word}' chưa có trong từ điển.")

def hien_thi_tu_dien():
    if dictionary:
        print(" Từ điển hiện tại:")
        for word, meaning in dictionary.items():
            print(f"- {word}: {meaning}")
    else:
        print(" Từ điển hiện đang trống.")


while True:
    print("\n===== ỨNG DỤNG TỪ ĐIỂN =====")
    print("1. Thêm từ mới")
    print("2. Xóa từ")
    print("3. Cập nhật nghĩa của từ")
    print("4. Tra cứu từ")
    print("5. Hiển thị toàn bộ từ điển")
    print("6. Thoát")

    choice = input(" Chọn chức năng (1-6): ")

    if choice == "1":
        them_tu()
    elif choice == "2":
        xoa_tu()
    elif choice == "3":
        cap_nhat_nghia()
    elif choice == "4":
        tra_cuu()
    elif choice == "5":
        hien_thi_tu_dien()
    elif choice == "6":
        print(" Thoát chương trình. Tạm biệt!")
        break
    else:
        print(" Lựa chọn không hợp lệ, vui lòng nhập lại.")
