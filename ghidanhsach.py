import csv
students = [
    {'MaSV': 'SV01', 'HoTen': 'Nguyen Van A', 'Tuoi': 20, 'ChuyenNganh': 'CNTT'},
    {'MaSV': 'SV02', 'HoTen': 'Tran Thi B', 'Tuoi': 21, 'ChuyenNganh': 'Kinh te'},
    {'MaSV': 'SV03', 'HoTen': 'Le Van C', 'Tuoi': 19, 'ChuyenNganh': 'Marketing'}
]

with open('sinhvien.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['MaSV', 'HoTen', 'Tuoi', 'ChuyenNganh'])
    writer.writeheader()
    writer.writerows(students)

print(" Đã ghi dữ liệu vào file sinhvien.csv")
with open('sinhvien.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print("\n Danh sách sinh viên đọc từ file:")
    for row in reader:
        print(row)
