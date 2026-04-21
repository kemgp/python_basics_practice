def main():
    score = int(input("Enter your score: "))
    
 #   if score >= 90 and score <= 100:
 #       print("You got an A!")
 #   elif score >= 80 and score < 90:
 #       print("You got a B!")
 #   elif score >= 70 and score < 80: 
 #       print("You got a C!")
 #   elif score >= 60 and score < 70:
 #       print("You got a D!")
 #   elif score >= 0 and score < 60:
 #       print("You got an F!")
 #   else:
 #       print("Invalid score. Please enter a score between 0 and 100.")
 
#inefficient compared to
 #   if 90<= score <= 100:
 #       print("You got an A!")
 #   elif 80 <= score < 90:
 #       print("You got a B!")
 #   elif 70 <= score < 80:
 #       print("You got a C!")
 #   elif 60 <= score < 70:
 #       print("You got a D!")
 #   elif 0 <= score < 60:
 #       print("You got an F!")
 #   else:
 #       print("Invalid score. Please enter a score between 0 and 100.")
 
 #further simplified to
    if score >=90:
        print("You got an A!")
    elif score >= 80:
        print("You got a B!")
    elif score >= 70:
        print("You got a C!")
    elif score >= 60:
        print("You got a D!")
    else:
        print("You got an F!")
main()