# THERE ARE TWO TYPES OF LOOPS IN PYTHON: FOR & WHILE
# FOR LOOPS
# In programming, a loop means executing something repetitively.
# And it's really powerful because it means we can run things thousands or millions of times.
# You can replace that 'letter' position with anything such as 'i', 'var', 'item', 'element' because they are all variable names which we created
# An iterable is an object which can be looped over or iterated over with the help of a loop.
# It also means that it's capable of returning its members one at a time.
# Iterable is, anything that you can loop over and in Python, many objects are iterable, meaning that we can iterate over each element of that sequence.
# These are iterable words: => Strings, lists, tuples, sex dictionaries and even files are all eatables.

# # Lets iterate STRINGS
# for letter in 'Python':
#     print(letter) # This is only one line of code
#
# # Lets iterate LIST
# for letter in [1, 2, 3]:
#     print(letter) # This is only one line of code
#
# # Lets iterate TUPLES
# for letter in (1, 2, 3):
#     print(letter) # This is only one line of code
#
# # Lets iterate SETS
# for letter in {1, 'a', 'b'}:
#     print(letter) # This is only one line of code
#
# # This are 3 lines of code
# for letter in 'Python1':
#     print(letter) # This is only one line of code
#     print('bye') # This is only one line of code
#     print('###########') # This is only one line of code

my_str = input('Enter something:')
vowels = 'aeiou'
for item in my_str:
    if item in vowels:
        print(item, end=' ') # This means that the print function won't add a backslash n after printing the string, but the whitespace.
                            # And all the vowels will be on the same line.