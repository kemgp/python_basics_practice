def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percent would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
def dollars_to_float(d):
    conv_d = d
    conv_d = conv_d.replace("$", "")
    conv_d = float(conv_d)
    return conv_d
    
def percent_to_float(p):
    conv_p = p
    conv_p = conv_p.replace("$", "")
    conv_p = float(conv_p)
    conv_p = conv_p/100
    return conv_p
    
    
main()