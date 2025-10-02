chieu_cao = int(input("Nhập chiều cao của tam giác: "))
print("\n--- Tam giác vuông (hướng lên) ---")
for i in range(1, chieu_cao + 1):
    print("*" * i)
print("\n--- Tam giác vuông (hướng xuống) ---")
for i in range(chieu_cao, 0, -1):
    print("*" * i)
print("\n--- Tam giác cân ---")
for i in range(1, chieu_cao + 1):
    print(" " * (chieu_cao - i) + "*" * (2*i - 1))
