milesDriven = 0
gallons = 0
totalMiles = 0
totalGallons = 0

num1 = input("enter the miles driven or -1 to exit")
num2 = input("enter the gallons used ")

num1 = int(num1)
num2 = int(num2)

while (num1 != -1):
    totalMiles =  totalMiles + num1
    totalGallons =  totalGallons + num2

    milePergalon = float(num1 / num2)
    print("miles per gallon is %f" %milePergalon)

    num1 = input("enter the miles driven or -1 to exit ")
    num2 = input("enter the gallons used ")

    num1 = int(num1)
    num2 = int(num2)

final = float(totalMiles / totalGallons)
print("final miles per gallon is %f"%final)

