# List Comprehensions =========================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Regular for loop to copy a list
print()
print('Regular for loop to copy a list')
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# Same result as above but with a list comprehension
print()
print('Same result as above but with a list comprehension')
my_list = [n for n in nums]
print(my_list)

# Regular for loop to return n squared from a list
print()
print('Regular for loop to return n squared as a new list')
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# Same result as above but with a list comprehension
print()
print('Same result as above but with a list comprehension')
my_list = [n * n for n in nums]
print(my_list)

# Regular for loop to return even indices from a list
print()
print('Regular for loop to return even indices from a list')
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# Same result as above but with a list comprehension
print()
print('Same result as above but with a list comprehension')
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# Regular for loop to return tuples of (letter, num) for 'abcd' and '0123'
print()
print('Regular for loop to return even indices from a list')
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# Same result as above but with a list comprehension
print()
print('Same result as above but with a list comprehension')
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehensions ===================================================

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# Regular for loop to return a dictionary from 2 lists
print()
print('Regular for loop to return even indices from a list')
my_dict = {}
for name, hero in zip(names, heroes):
    for num in range(4):
        my_dict[name] = hero
print(my_dict)

# Same result as above but with a dictionary comprehension
print()
print('Same result as above but with a list comprehension')
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# Same result as above but without name == 'Peter'
print()
print('Same result as above but without name == \'Peter\'')
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

# Set Comprehensions ==========================================================

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

# Regular for loop to copy a list into a set (sets cannot have duplicate vals)
my_set = set()
print()
print('Regular for loop to copy a list into a set')
for n in nums:
    my_set.add(n)
print(my_set)

# Same result as above but with a set comprehension
print()
print('Same result as above but with a set comprehension')
my_set = {n for n in nums}
print(my_set)
