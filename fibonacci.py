def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  
while True:
    try:
        n = int(input("Nhập số lượng phần tử Fibonacci cần in: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương!")
    except ValueError:
        print("Dữ liệu không hợp lệ, hãy nhập số nguyên!")
print(f"\n{n} số Fibonacci đầu tiên là:")
fibonacci(n)
print()  
