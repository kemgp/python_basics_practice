def main():
    firstNum = int(input("Input first number: "))
    secondNum = int(input("Input second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    
    if operator == "+":
        print(f"{firstNum + secondNum}")
    elif operator == "-":
        print(f"{firstNum - secondNum}")
    elif operator == "*":
        print(f"{firstNum * secondNum}")
    elif operator == "/":
        if secondNum != 0:
            print(f"{firstNum / secondNum}")
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid operator")
        
main()
        