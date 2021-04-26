

day = input()
fruit = input()
quantity = float(input())
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        print(f"{quantity* 2.50}")
    if fruit == "apple":
        print(f"{quantity * 1.20}")
    if fruit == "orange":
        print(f"{quantity * 0.85}")
    if fruit == "grapefruit":
        print(f"{quantity * 1.45}")
    if fruit == "kiwi":
        print(f"{quantity * 2.70}")
    if fruit == "pineapple":
        print(f"{quantity * 5.50}")
    if fruit == "grapes":
        print(f"{quantity * 3.85}")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        print(f"{quantity * 2.70}")
    if fruit == "apple":
        print(f"{quantity * 1.25}")
    if fruit == "orange":
        print(f"{quantity * 0.90}")
    if fruit == "grapefruit":
        print(f"{quantity * 1.60}")
    if fruit == "kiwi":
        print(f"{quantity * 3.00}")
    if fruit == "pineapple":
        print(f"{quantity * 5.60}")
    if fruit == "grapes":
        print(f"{quantity * 4.20}")
else:
    print("error")
