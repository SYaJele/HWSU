

day = int(input())
if day in range(1, 8):
    if day == 1:
        print("Monday")
    if day == 2:
        print("Tuesday")
    if day == 3:
        print("Wednesday")
    if day == 4:
        print("Thursday")
    if day == 5:
        print("Friday")
    if day == 6:
        print("Saturday")
    if day == 7:
        print("Sunday")
else:
    print("Error")