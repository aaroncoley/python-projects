def chat_bot():
    print("welcome!")
    response = input("what can I help you with?\n")
    if (response == "calculate"):

        func = input("what do you wanna calculate")
        num1 = int(input("what's your first number"))
        num2 = int(input("what's your second number"))

        result = 0

        if (func == "addition"):
            result = num1 + num2
        elif (func == "substraction"):
            result = num1 - num2
        elif (func == "multiplication"):
            result = num1 * num2
        elif (func == "divison"):
            result = num1 / num2
        elif (func == "power"):
            result = num1 ** num2

        print("Your result is ", result)
        
chat_bot()