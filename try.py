def main():
    name = input("Whats your name? ")
    name = name.capitalize().strip()
    hello(name)

def hello(to="world"):
    print("hello,", to)


main()