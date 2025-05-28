import time

#   for loop = a statement that will execute its block of code a limited number of times
#              while loop = unlumited
#              for loop = limited

# prints every numbner from 0 to 9
for i in range(10):
    print(i)

# prints loop from 50 to 99, but in steps of 5
for i in range(50,100, 5):
    print(i)

# prints loop through text
for i in 'Zaid Jilla':
    print(i)

# creates a timer
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy New Year!')
