def main():
    calculate()
        

def calculate():
    continueCalculation = True
    while continueCalculation == True:
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
            
        next_calculation = input("Do you want to calculate again? (Yes/No)")
        if next_calculation == "No":
            continueCalculation = False
    



main()
        