# slicing = creating a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = 'Zaid Jilla'
# first name
first_name = name[:4]
print(first_name)
# last name
last_name = name[5:]
print(last_name)
# funky name, every second character
funky_name = name[::2]
print(funky_name)
# reversed name
reversed_name = name[::-1]
print(reversed_name)

website1 = 'https://google.com'
website2 = 'https://facebook.com'
# each string has a positive and negative index
# we know that the first 7 characters are https://
# and the last 4 characters are .com
# so we can slice the string from the 7th character to the 4th last character
sliceit = slice(7,-4)

print(website1[sliceit])
print(website2[sliceit])