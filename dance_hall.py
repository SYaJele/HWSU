
import math

l = float(input())*100
w = float(input())*100
a = float(input())*100
S = l * w
s = a * a
skameika = S / 10
S = S - (s + skameika)
x = S / 7040
print(math.floor(x))
