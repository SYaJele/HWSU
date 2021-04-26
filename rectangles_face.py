

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1 - x2)
height = abs(y2 - y1)

print(f"{length * height:.2f}")
print(f"{2 * (length + height):.2f}")