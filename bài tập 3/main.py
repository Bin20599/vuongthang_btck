import os

file_nguon = "nguon.txt"
file_dich = "dich.txt"

try:
    if not os.path.exists(file_nguon):
        raise FileNotFoundError

    with open(file_nguon, 'r', encoding='utf-8') as f_nguon:
        noidung = f_nguon.read()

    with open(file_dich, 'w', encoding='utf-8') as f_dich:
        f_dich.write(noidung)

    print(" Sao chép nội dung thành công!")
    print(f" File nguồn: {file_nguon}")
    print(f" File đích: {file_dich}")

except FileNotFoundError:
    print(" Không tìm thấy file nguồn!")
    print(f" Hãy chắc chắn rằng file '{file_nguon}' nằm trong thư mục: {os.getcwd()}")
