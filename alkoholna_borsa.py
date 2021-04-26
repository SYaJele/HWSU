

price_wiskey = float(input())
price_rakia = price_wiskey / 2
beer = float(input()) * (price_rakia - (0.8 * price_rakia))
wine = float(input()) * (price_rakia - (0.4 * price_rakia))
rakia = float(input()) * price_rakia
wiskey = float(input()) * price_wiskey
print(f"{(wiskey + rakia + wine + beer):.2f}")
