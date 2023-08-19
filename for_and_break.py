# For, else, and break statements

for number in range(10):
    print(number)
    if number == 5:
        break

print('Outside for')

for letter in 'Python':
    if letter == 'o':
        print('letter is o and I\'m breaking out of the loop ...')
        break
    print(letter)

for n in range(0, 20):
    if n % 13 == 0:
        print('there is a number divisible by 13 in the range. Breaking out ...')
        break
else: # This belong to for
    print('There is no number divisible by 13 in the range.')

for l in 'abc':  # Outer looop
    print(l)
    for n in range(3):  # Inner loop
        if n == 1:
            break
        print(n)