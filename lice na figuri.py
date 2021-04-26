figure = input()
if figure == "square":
    a = float(input())
    square_area = a * a
    print(f"{square_area:.3f}")
if figure == "rectangle":
    a1 = float(input())
    b1 = float(input())
    rectangle_area = a1 * b1
    print(f"{rectangle_area:.3f}")
if figure == "circle":
    a2 = float(input())
    circle_area = 3.14 * (a2 * a2)
    print(f"{circle_area:.3f}")
if figure == "triangle":
    a3 = float(input())
    h = float(input())
    triangle_area = (a3 * h) / 2
    print(f"{triangle_area:.3f}")