# FORMATTING STRINGS

first_name = 'John'
last_name = 'Smith'
age = 40
print('Hello ' + first_name + ' ' + last_name + '! you are '  + str(age) + ' years old.')
# f added at beginning is called an F string and you can use either f or F
print(f'Hello {first_name} {last_name}! You are {age} years old.') # f added at beginning is called an F string.

s = f'{2.3 * 4.2 / 5.1:.4f}' # The .4f will format the value to 4 decimal
print(s)

# To convert celsius to fahrenheit: USE => fahrenheit = celsius * 1.8 + 32
celsius = 15.4
print(f'{celsius} degrees Celsius = {celsius * 1.8 + 32} degrees Fahrenheit.')