

length = int(input())
width = int(input())
height = int(input())
taken_space = float(input())
if length in range(10, 500):
        if width >= 10 and width <= 300:
                if height >= 10 and height <= 200:
                         if taken_space >= 0.000 and taken_space <= 100.000:
                                 print(f"{(((length * width * height) * 0.001) * (1 - (taken_space * 0.01))):.3f}")
