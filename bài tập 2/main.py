import string
import os

# Đặt tên file
filename = "vanban.txt"

# Kiểm tra xem file có tồn tại trong thư mục hiện tại không
print("Thư mục hiện tại:", os.getcwd())
print("File tồn tại?", os.path.exists(filename))

try:
    # Kiểm tra file có tồn tại không trước khi mở
    if not os.path.exists(filename):
        raise FileNotFoundError

    # Đọc nội dung file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Chuyển toàn bộ thành chữ thường
    content = content.lower()

    # Loại bỏ dấu câu
    for ch in string.punctuation:
        content = content.replace(ch, '')

    # Tách các từ trong nội dung
    words = content.split()

    # Đếm tổng số từ
    total_words = len(words)

    # Hiển thị kết quả
    print("\nNội dung trong file:")
    print(content)
    print("\nTổng số từ trong file là:", total_words)

except FileNotFoundError:
    print("\n❌ Không tìm thấy file!")
    print("➡ Hãy chắc chắn rằng file 'vanban.txt' nằm cùng thư mục với chương trình này.")
    print("👉 Thư mục hiện tại là:", os.getcwd())

