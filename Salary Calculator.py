name = input("enter emplyee name :")
salPerHour = input("enter the salary pays for an hour :")
hours = input("enter the hours worked :")

salPerHour = float(salPerHour)
hours = float(hours)

if (hours < 40):
    total = float(salPerHour * hours)
    print("your total salary is %f" %total)
else:
    total = float((40 * salPerHour) + ((hours - 40)*salPerHour) / 2)
    print("your total salary is %f" % total)