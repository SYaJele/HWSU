screening_type = input()
redove = int(input())
koloni = int(input())
income = 0
cinema_capacity = redove * koloni
if screening_type == "P":
    income = cinema_capacity * 12.00
elif screening_type == "N":
    income = cinema_capacity * 7.50
elif screening_type == "D":
    income = cinema_capacity * 5.00
print(f"{income:.2f}")