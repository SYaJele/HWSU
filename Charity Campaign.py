

days = int(input())
sladkari = int(input())
torti = int(input()) * 45
gofreti = int(input()) * 5.80
palachinki = int(input()) * 3.20
sladkishi = (torti + gofreti + palachinki)
print(f"{((days * (sladkishi) * sladkari) - 1/8*(days * (sladkishi) * sladkari)):.2f}")