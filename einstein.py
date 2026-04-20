def main():
    mass = int(input("What is the mass? "))
    print(converter(mass))
    
def converter(num):
    conversion = int(300000000**2)
    converted = int(num)
    return (conversion * converted)
    
main()