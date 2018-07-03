import datetime

person = {'name': 'Arin', 'age': 31}
my_list = ['Arin', 31]

print()
print('Basic Concatenation:')
sentence = 'My name is ' + person['name'] + ' and I am ' + str(
    person['age']) + ' years old.'
print(sentence)

print()
print('Using format() Function Without Indexing:')
sentence = 'My name is {} and I am {} years old. Again, my name is {}.'.format(
    person['name'], person['age'], person['name'])
print(sentence)

print()
print('Using format() Function With Indexing:')
sentence = 'My name is {0} and I am {1} years old. Again, my name is {0}.' \
    .format(person['name'], person['age'])
print(sentence)

print()
print('Using format() Function With Indexing and Passing Whole Dictionary:')
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

print()
print('Using format() Function With Indexing and Passing Unpacked Dictionary:')
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

print()
print('Using format() Function With Indexing and Passing Whole List:')
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(my_list)
print(sentence)

print()
print('Using format() Function With Indexing and Passing Class Instance:')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Arin', 31)
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(person1)
print(sentence)

print()
print('Using format() Function With kwargs:')
sentence = 'My name is {name} and I am {age} years old.'.format(name='Arin',
                                                                age=31)
print(sentence)

print()
print('Using format() With Numbers:')
for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)

print()
print('Using format() With Numbers and 0 Padding (Formatting the Values):')
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)
for i in range(1, 11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

print()
print('Using format() With Numbers and Trim Decimals (Formatting the Values):')
pi = 3.14159265
sentence = 'The value of Pi is {:.2f}'.format(pi)
print(sentence)
sentence = 'The value of Pi is {:.3f}'.format(pi)
print(sentence)

print()
print(
    'Using format() With Numbers and Comma Delimiter (Formatting the Values):')
sentence = '1 MB is equal to {:,} bytes'.format(1000 ** 2)
print(sentence)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000 ** 2)
print(sentence)

print()
print('Using format() With Date Objects:')
my_date = datetime.datetime(2018, 9, 24, 12, 30, 45)
sentence = '{}'.format(my_date)
print(sentence)
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)
