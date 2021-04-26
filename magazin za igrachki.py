vacation = float(input())
puzzle = int(input())
dolls = int(input())
teddy_bears = int(input())
minion = int(input())
truck = int(input())
sum = (puzzle * 2.60) + (dolls * 3) + (teddy_bears * 4.10) + (minion * 8.20) + (truck * 2)
quantity = puzzle + dolls + teddy_bears + minion + truck
if quantity > 50:
    discount = sum * 0.25
    end_price = sum - discount
    rent = end_price * 0.1
    profit = end_price - rent
    if profit > vacation:
        money = profit - vacation
        print(f"Yes! {money:.2f} lv left.")
    if profit < vacation:
        money = profit - vacation
        print(f"Not enough money! {money:.2f} lv needed.")
if quantity <= 50:
    rent1 = sum * 0.1
    profit1 = sum - rent1
    if profit1 > vacation:
        money1 = profit1 - vacation
        print(f"Yes! {money1:.2f} lv left.")
    if profit1 < vacation:
        money1 = profit1 - vacation
        print(f"Not enough money! {money1:.2f} lv needed.")