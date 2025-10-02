n = int(input("Nhập số lượng số chẵn cần in: "))
count = 0
number = 2
print(f"\n{n} số chẵn đầu tiên là:")
while count < n:
    print(number, end=" ")
    number += 2 
    count += 1   
print()
