so_tien = float(input("Nhập số tiền cần chuyển đổi: "))
tien_nguon = input("Nhập loại tiền tệ nguồn (USD, VND, EUR): ").upper()
tien_dich = input("Nhập loại tiền tệ đích (USD, VND, EUR): ").upper()

ty_gia = {
    "USD": 1.0,
    "VND": 25000.0,
    "EUR": 0.9
}
if tien_nguon not in ty_gia or tien_dich not in ty_gia:
    print("Loại tiền tệ không hợp lệ!")
else:
    usd = so_tien / ty_gia[tien_nguon]
    so_tien_quy_doi = usd * ty_gia[tien_dich]
    print(f"{so_tien:.2f} {tien_nguon} = {so_tien_quy_doi:.2f} {tien_dich}")
