accNo = input("please enter the account number :")
beginningBalance = input("enter the beginning balance of the month :")
totalCharges = input("please enter the total of charges :")
totalOfCredits = input("please enter the total of credits applied in this month :")
allowedCredit = input("please enter the allowed credit limit :")

beginningBalance = int(beginningBalance)
totalCharges = int(totalCharges)
totalOfCredits = int(totalOfCredits)
allowedCredit = int(allowedCredit)

finalBalance = beginningBalance + totalCharges - totalOfCredits

if (finalBalance < allowedCredit):
    print("credit limit exceeded !!")
else:
    print("get money")