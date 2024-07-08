def calculator(num1, num2, func):
    if (func == "addition"):
        print(num1 + num2)
    elif (func == "substraction"):
        print(num1 - num2)
    elif (func == "multiplication"):
        print(num1 * num2)
    elif (func == "divison"):
        print(num1 / num2)
    elif (func == "power"):
        print(num1 ** num2)
    else:
        print ("error")
    calculator(3,6,"subtraction")
    calculator(4,4,"multiplication")
    calculator(5,6,"addition")
    calculator(12,3,"divison")
    calculator(2,3,"power")