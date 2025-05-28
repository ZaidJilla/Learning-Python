# dictionary = A changable, unordered collection of unique key:value pairs
# they are fast because they use hashing, allow us to access a value quickly

capitals = {
    'USA': 'Washington, D.C.',
    'India': 'New Delhi',
    'Chuna': 'Beijing',
    'Russia': 'Moscow'}
print('------')

print(capitals['Russia'])

print('------')

print(capitals.get('Germany'))

print('------')

print(capitals.keys())

print('------')

print(capitals.values())

print('------')

print(capitals.items())

print('------')

capitals.update({'Germany':'Berlin'})

for key, value in capitals.items():
    print(f'The capital of {key} is {value}')