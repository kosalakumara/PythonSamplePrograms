'''demo program of demonstrating break statement'''
magicnumber = 99 #initializing the magic number

for x in range(100):
    if x is magicnumber:
        print("magic number found",end=" ")
        print("the number is ",x)
        break

    else:
        print("not found current number is ",x)