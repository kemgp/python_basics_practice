def main():
    name = input("What is your name? ")
    name = name.capitalize() #capitalize name for comparison!
    
#    if name =="Harry" or name == "Hermione" or name == "Ron":
#        print("Gryffindor")
#    elif name == "Draco":
#        print("Slytherin")
#    elif name == "Luna":
#        print("Ravenclaw")
#    elif name == "Neville":
#        print("Hufflepuff")
#    else:
#        print("I don't know which house you belong to")

#can be made more by using match statement, which is more efficient because it only checks for the specific cases instead of checking for multiple conditions in an if statement

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case "Luna":
            print("Ravenclaw")
        case "Neville":
            print("Hufflepuff")
        case _:
            print("I don't know which house you belong to")

main()