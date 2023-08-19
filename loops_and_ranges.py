# HOW TO USE LOOPS AND RANGES

s = 0
for n in range(101): # is the same as range(0, 101, 1)
    s += n
print(f'Sum: {s}') # This line of code is not part of the loop and it will return 5050 as value

# Another example making print part of the loop by identing by four spaces of tab
for n in range(10): # Begin from 0 => 9 & stop at 10
    print('Do something', n) # Begin from 0 => 9 & stop at 10

# Similar example making print part of the loop by identing by four spaces of tab
for _ in range(10):
    print('Do something', _)

import random
names = ['Diana', 'Paul', 'Ana', 'Dan', 'Victor', 'Marry', 'Alexander', 'Maria', 'Jeff', 'Bob', 'Bill', 'Angie']
for _ in range(3):
    print(f'Choosing winner. Round {_} ...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('########')