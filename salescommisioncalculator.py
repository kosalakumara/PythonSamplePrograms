Items = [239.99,129.75,99.95,3,50.89]

total = 0
itemNo = input("please enter the item no. or -1 to exit : ")
itemNo = int(itemNo)

while(itemNo != -1):
    total = total + Items[itemNo-1]
    itemNo = input("please enter the item no. or -1 to exit : ")
    itemNo = int(itemNo)

balance = float((total * 9)/100) + 200

print("your final salary is %f" %balance)