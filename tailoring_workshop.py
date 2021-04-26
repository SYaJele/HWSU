

number = int(input())
length = float(input())
width = float(input())
p = (number * (length + 2 * 0.30) * (width + 2 * 0.30))
c = number * (length/2) * (length/2)
USD = (p * 7) + (c * 9)
print(f" {USD:.2f} USD")
print(f" {USD * 1.63:.2f} BGN")