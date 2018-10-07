def calculateCharges(time):
    charge = "unknown"
    if time is 24:
        charge = 10.00
    elif time is 3 | time < 3:
        charge = 2
    else:
        charge = 2 + (time % 3) * 0.5

    print("your total charge is",charge)

calculateCharges(3)
calculateCharges(24)
calculateCharges(4)