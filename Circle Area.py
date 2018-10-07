def circleArea(radius):
    area = 3.14 * (radius * radius)
    return area

def getInput():
    rad = input("enter the radius of the circle :")
    rad = float(rad)
    print(circleArea(rad))

getInput()