print("=== CHƯƠNG TRÌNH TÌM PHẦN TỬ TRONG A NHƯNG KHÔNG CÓ TRONG B ===")
input_A = input("Nhập danh sách A (các số cách nhau bởi dấu cách): ")
input_B = input("Nhập danh sách B (các số cách nhau bởi dấu cách): ")

list_A = list(map(int, input_A.split()))
list_B = list(map(int, input_B.split()))

print("\nDanh sách A:", list_A)
print("Danh sách B:", list_B)
set_A = set(list_A)
set_B = set(list_B)
print("\nTập hợp A (loại bỏ trùng lặp):", set_A)
print("Tập hợp B (loại bỏ trùng lặp):", set_B)
diff = set_A.difference(set_B)   
print("\n=== KẾT QUẢ ===")
if diff:
    diff_sorted = sorted(list(diff))
    print("Các phần tử có trong A nhưng không có trong B là:", diff_sorted)
else:
    print("Không có phần tử nào thuộc A mà không có trong B.")

print("\n=== KẾT THÚC CHƯƠNG TRÌNH ===")
