def addNumbers(*args):
    total = 0
    for a in args:
        total += a
    print("the total is",total)


addNumbers(3,4,5,3)
addNumbers()
addNumbers(33)