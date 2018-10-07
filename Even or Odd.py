def getInput():
    num1 = input("please enter the value")
    num1 = int(num1)
    isEven(num1)

def isEven(num):
    if num % 2 is 0:
        print("even number")
    else:
        print("odd number")

getInput()