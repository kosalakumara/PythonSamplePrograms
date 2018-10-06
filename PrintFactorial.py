num = input("please enter the number ")
num = int(num)

total = 1

for x in range(1,(num + 1)):
    total = total * x
    print("current total is %i"%total)

print("the factorial is %i "%total)