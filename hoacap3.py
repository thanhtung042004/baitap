# Khai báo các hệ số của hệ phương trình
a1, b1, c1 = 1.0, 1.0, 2.0       # Phương trình 1: x + y = 2
a2, b2, c2 = 58.0, 60.0, 5838.2  # Phương trình 2: 58x + 60y = 5838.2

# Tính toán định thức
D = a1 * b2 - a2 * b1         # Định thức chính
Dx = c1 * b2 - c2 * b1        # Định thức theo x
Dy = a1 * c2 - a2 * c1        # Định thức theo y

# Kiểm tra nếu D bằng 0 để xác định hệ có nghiệm hay không
if D == 0:
    if Dx == 0 and Dy == 0:
        print("Hệ phương trình có vô số nghiệm.")
    else:
        print("Hệ phương trình vô nghiệm.")
else:
    # Tính nghiệm x và y
    x = Dx / D
    y = Dy / D
    print("Nghiệm của hệ phương trình là:")
    print(f"x = {x}")
    print(f"y = {y}")
