

city = input()
sales = float(input())
if sales > 0 and sales <= 500:
    if city == "Sofia":
        price = sales * 0.05
        print(f"{price:.2f}")
    if city == "Varna":
        price = sales * 0.045
        print(f"{price:.2f}")
    if city == "Plovdiv":
        price = sales * 0.055
        print(f"{price:.2f}")
elif sales > 500 and sales <= 1000:
    if city == "Sofia":
        price = sales * 0.07
        print(f"{price:.2f}")
    if city == "Varna":
        price = sales * 0.075
        print(f"{price:.2f}")
    if city == "Plovdiv":
        price = sales * 0.08
        print(f"{price:.2f}")
elif sales > 1000 and sales <= 10000:
    if city == "Sofia":
        price = sales * 0.08
        print(f"{price:.2f}")
    if city == "Varna":
        price = sales * 0.1
        print(f"{price:.2f}")
    if city == "Plovdiv":
        price = sales * 0.12
        print(f"{price:.2f}")
elif sales > 10000:
    if city == "Sofia":
        price = sales * 0.12
        print(f"{price:.2f}")
    if city == "Varna":
        price = sales * 0.13
        print(f"{price:.2f}")
    if city == "Plovdiv":
        price = sales * 0.145
        print(f"{price:.2f}")
else:
    print("error")
