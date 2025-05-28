# lists = used to store multiple items in a single variable

food = ['pizza', 'burger', 'hotdog', 'pasta', 'ice cream']

print(food)

print(food[0])

# adds an item to the end of the list
food.append('sushi')
# removes an item from the list
food.remove('hotdog')
# removes the last item from the list
food.pop()
#inserts an item at a specified position
food.insert(0, 'cake')
# sorts the list aphabetically
food.sort()
# clears the list
# food.clear()


for x in food:
    print(x)

