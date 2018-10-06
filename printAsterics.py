num = input("please enter the number of asterics ")
num = int(num)

for x in range(0,num):
    for y in range(0,x+1):
        print("*",end = "")
    print()