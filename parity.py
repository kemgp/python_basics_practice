def main():
    odd_or_even = int(input("Enter a number: "))
    if is_even(odd_or_even):
        print("The number is even")
    else:
        print("The number is odd")

        
#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

#simplified to
#def is_even(n):
#    return True if n % 2 == 0 else False

#further simplified to
def is_even(n):
    return n % 2 == 0 #no need for if statement because n % 2 == 0 already evaluates to True or False

main()