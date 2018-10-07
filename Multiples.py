def isMultiple(value1,value2):
    if value1 % value2 is 0:
        return 1
    else:
        return 0


def invoke():
    if isMultiple(11,4):
        print("is a multiple")
    else:
        print("not a multiple")

invoke()