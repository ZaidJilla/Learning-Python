# tuple = collection which is ordered and unchangable used to group together related data

student = ('Zaid', 18, 'Male')
print(student.count('Zaid'))  
print(student.index('Male'))

for i in student:
    print(i)

if 'Zaid' in student:
    print('Zaid is here')