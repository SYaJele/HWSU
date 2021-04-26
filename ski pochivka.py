day = int(input())
room = input()
assessment = input()
if day in range(1, 10):
    if room == "room for one person":
        nights_price = (day - 1) * 18.00
        if assessment == "positive":
            print(f"{nights_price + (nights_price * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{nights_price - (nights_price * 0.1):.2f}")
    if room == "apartment":
        nights_price = (day - 1) * 25.00
        sum = nights_price * 0.30
        discount = nights_price - sum
        if assessment == "positive":
            print(f"{discount + (discount * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{discount - (discount * 0.1):.2f}")
    if room == "president apartment":
        nights_price = (day - 1) * 35.00
        sum = nights_price * 0.1
        discount = nights_price - sum
        if assessment == "positive":
            print(f"{discount + (discount * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{discount - (discount * 0.1):.2f}")
if day in range(10, 16):
    if room == "room for one person":
        nights_price = (day - 1) * 18.00
        if assessment == "positive":
            print(f"{nights_price + (nights_price * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{nights_price - (nights_price * 0.1):.2f}")
    if room == "apartment":
        nights_price = (day - 1) * 25.00
        sum = nights_price * 0.35
        discount = nights_price - sum
        if assessment == "positive":
            print(f"{discount + (discount * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{discount - (discount * 0.1):.2f}")
    if room == "president apartment":
        nights_price = (day - 1) * 35.00
        sum = nights_price * 0.15
        discount = nights_price - sum
        if assessment == "positive":
            print(f"{discount + (discount * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{discount - (discount * 0.1):.2f}")
if day > 15:
    if room == "room for one person":
        nights_price = (day - 1) * 18.00
        if assessment == "positive":
            print(f"{nights_price + (nights_price * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{nights_price - (nights_price * 0.1):.2f}")
    if room == "apartment":
        nights_price = (day - 1) * 25.00
        sum = nights_price * 0.50
        discount = nights_price - sum
        if assessment == "positive":
            print(f"{discount + (discount * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{discount - (discount * 0.1):.2f}")
    if room == "president apartment":
        nights_price = (day - 1) * 35.00
        sum = nights_price * 0.2
        discount = nights_price - sum
        if assessment == "positive":
            print(f"{discount + (discount * 0.25):.2f}")
        elif assessment == "negative":
            print(f"{discount - (discount * 0.1):.2f}")
