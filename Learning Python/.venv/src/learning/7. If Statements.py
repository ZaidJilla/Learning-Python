# if statement =  a block of code that will executre if its condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You are not born yet!")
else:
    print("You are a child!")