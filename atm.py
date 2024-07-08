def atm():
    num = int(input ("What is your starting amnt"))
    process = input ("what do you want to do?")
    if process = "deposit":
        depositant = int (input ("How much do you want to deposit"))
        num = depositant + num
        print("Total is: " + str (num))

    elif process = "withdrawal":
        withdrawalant = int (input("how much would you like to withdraw"))
        num = withdrawalamnt - num
        print("Total is: " + str(num))
    else:
        print ("Error")

atm()