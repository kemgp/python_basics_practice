#practicing conditionals

#comparison
def comparison():
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))

    if num1 < num2:
        print("The first number is less than the second number")
    elif num1 > num2:
        print("The first number is greater than the second number")
    else:
        print("The two numbers are equal")