class problem1:
    def calculate(self):
        total = 0
        for x in range(1000):
            print("entered value ",x)
            print(end="")
            if ((x % 3 == 0) | (x % 5 == 0)):
                total = total + x

        print("the total is ",total)


t = problem1()
t.calculate()