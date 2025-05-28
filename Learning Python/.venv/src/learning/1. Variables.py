# variable = a container for a value. Behaves as the value that it contains.

# string variable
first_name = 'Zaid'
last_name = 'jilla'
full_name = first_name.capitalize()+ ' '+ last_name.capitalize()
print("Hello", full_name)
#print(type(name))

# integer variables
age = 18
age += 1 
print(age)
print('your age next year is:', str(age))
#print(type(age))

# float variables
height = 250.5
print(height)
print('Your height is', str(height)+'cm')
#print(type(height))

# boolean variables
human = True
print('Are you a human:', str(human))
#print(type(human))

# multiple assignment = allows us to assign multiple variables at the same time in one line of code
#name = 'Zaid'
#age = 18
#attractive = True
name, age, attractive = 'Zaid', 18, True
print('Name:', name)
print('Age:', age)
print('Attractive:', attractive)
