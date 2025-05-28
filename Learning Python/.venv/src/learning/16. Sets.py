# set = collection which is unordered, unindexed. No duplicate values
# faster than lists
utensils = {'fork', 'spoon', 'knife'}

utensils2 = {'fork', 'spoon', 'knife', 'fork'}

for x in utensils:
    print(x)

print('------')

for x in utensils2:
    print(x)

print('------')

utensils.add('napkin')
utensils.remove('fork')
for x in utensils:
    print(x)

print('------')

utensils.clear()
print(utensils)

print('------')

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup'}
utensils.update(dishes)
for x in utensils:
    print(x)