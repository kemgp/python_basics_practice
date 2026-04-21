x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

#originally used if x > y or x < y, but this is more efficient because it only checks if x and y are not equal, which is the only condition that matters when checking for equality

if x != y:
    print("The two numbers are not equal")
else:
    print("The two numbers are equal")