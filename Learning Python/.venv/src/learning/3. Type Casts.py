# type casting = converting the data type of a value to another data type

x = 1 # int
y = 2.5 # float
z = '3' # str
# you cannot do math with strings

# converting float to int, not a permnanent change
print(int(y)) 
print(y)

# converting float to int, permanent change
y = int(y) 
print(y)

# when would you need to convert an int or float to a string?
# print('X is'+ x)
# error: can only concatenate str (not "int") to str
print('X is '+ str(x))

