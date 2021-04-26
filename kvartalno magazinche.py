

product = input()
city = input()
quantity = float(input())
if city == "Sofia":
    if product == "coffee":
        print(f"{quantity * 0.50:.2f}")
    if product == "water":
        print(f"{quantity * 0.80:.2f}")
    if product == "beer":
        print(f"{quantity * 1.20:.2f}")
    if product == "sweets":
        print(f"{quantity * 1.45:.2f}")
    if product == "peanuts":
        print(f"{quantity * 1.60:.2f}")
if city == "Plovdiv":
    if product == "coffee":
        print(f"{quantity * 0.40:.2f}")
    if product == "water":
        print(f"{quantity * 0.70:.2f}")
    if product == "beer":
        print(f"{quantity * 1.15:.2f}")
    if product == "sweets":
        print(f"{quantity * 1.30:.2f}")
    if product == "peanuts":
        print(f"{quantity * 1.50:.2f}")
if city == "Varna":
    if product == "coffee":
        print(f"{quantity * 0.45:.2f}")
    if product == "water":
        print(f"{quantity * 0.70:.2f}")
    if product == "beer":
        print(f"{quantity * 1.10:.2f}")
    if product == "sweets":
        print(f"{quantity * 1.35:.2f}")
    if product == "peanuts":
        print(f"{quantity * 1.55:.2f}")
