import random

value = random.random()
print()
print('random float between 0 - 1 (NOT INCLUSIVE)')
print(value)

value = random.uniform(1, 10)
print()
print('Random float between a range (NOT INCLUSIVE)')
print(value)

value = random.randint(1, 10)
print()
print('Random int between a range (INCLUSIVE)')
print(value)

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
print()
print('Random choice from a list/dict/set/tuple/etc.')
print(value + ', Arin!')

# k= is the amount of times we want to select a random choice
# weights= is the likely hood that the corresponding value will be selected
print()
print('Random choices from a list/dict/set/tuple/etc.')
colors = ['Red', 'Blue', 'Green']
results = random.choices(colors, k=10)
print(results)
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

print()
print('Shuffle a list')
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

print()
print('Return a random but unique value from a list n times as a list')
hand = random.sample(deck, k=5)
print(hand)
