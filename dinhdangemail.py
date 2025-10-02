while True:   
    email = input("Nhập địa chỉ email: ").strip()    
    if "@" in email and "." in email:
        at_index = email.find("@")
        dot_index = email.rfind(".")
        if 0 < at_index < dot_index < len(email) - 1:            
            email = email.lower()
            print("Email hợp lệ:", email)
            break
        else:
            print(" Định dạng email không hợp lệ, vui lòng nhập lại.\n")
    else:
        print(" Email phải chứa ký tự '@' và '.', vui lòng nhập lại.\n")
