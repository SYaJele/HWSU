x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
if x1 < x2 and y1 < y2:
    if x1 < x and x < x2:
        if y1 < y and y < y2:
            print("Inside / Outside")
    if (x1 == x or x == x2) or (y1 == y or y == y2):
        print("Border")