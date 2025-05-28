# logical operators (and, or, not) = used to check if two or more conditional statements have been met

temp = int(input("What is the temprature outside? (C): "))

if temp>=0 and temp<=30:
    print("The temprature is good today!")
    print("Go outside and enjoy the weather!")
elif temp < 0 or temp > 30: 
    print("The temprature is not good today!")
    print("Stay inside!")