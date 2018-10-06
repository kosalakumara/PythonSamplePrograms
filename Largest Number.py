
number = input("please enter the number :")
number = int(number)

counter = 1
maximum = number

while(counter <= 10):

    if  maximum < number:
        maximum = number
    number = input("please enter the number :")
    number = int(number)

    counter = counter + 1



print("the maximum number is %f"%maximum)