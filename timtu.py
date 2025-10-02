data = input("Nhập danh sách các phần tử (cách nhau bởi dấu phẩy): ")
lst = [item.strip() for item in data.split(",")]
freq = {}  
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
max_count = max(freq.values())  
most_frequent = [key for key, value in freq.items() if value == max_count]
print("\n Kết quả:")
if len(most_frequent) == 1:
    print(f"Phần tử xuất hiện nhiều nhất là '{most_frequent[0]}' ({max_count} lần).")
else:
    print(f"Các phần tử xuất hiện nhiều nhất ({max_count} lần): {', '.join(most_frequent)}")
