def main():
    calculate()
        

def calculate():
    continueCalculation = True
    while continueCalculation == True:
        firstNum = int(input("Input first number: "))
        secondNum = int(input("Input second number: "))
        operator = input("Enter operator (+, -, *, /, or type exit to quit): ")
        
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
        elif operator.lower() == "exit":
            break
        else:
            print("Invalid operator!")
            continue
            
        nextCalculation = input("Do you want to calculate again? (Yes / No)")
        if nextCalculation.lower() == "yes":
            continue
        elif nextCalculation.lower() == "no":
            break
        else:
            print("Invalid input! Type yes or no")
            continue
main()
        