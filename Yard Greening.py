

square_meters = float(input())
price = 7.61
discount = 0.18
full_price = square_meters * price
discounted_price = discount * full_price
final_price = full_price - discounted_price
print(f"You need to pay {final_price:.2f} for the service.")
print(f"And the discount that you get is {discounted_price:.2f}.")