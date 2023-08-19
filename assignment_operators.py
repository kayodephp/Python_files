# Equals (=)
a = 5

# Plus equals (+=)
a += 2 # This is a shorthand or shortcut for a = a + 2 = 7
print(a)

# Minus equals (-=) (Note: the last value of a is 7)
a -= 3 # This is a shorthand or shortcut for a = a - 3 = 4
print(a)

# Star equals (*=) (Note: the last value of a is 4)
a *= 3 # This is a shorthand or shortcut for a = a * 3 = 12
print(a)

# Star equals (/=) (Note: the last value of a is 12)
a /= 2 # This is a shorthand or shortcut for a = a / 2 = 6.0
print(a)

# Star equals (**=) (Note: the last value of a is 6)
a **= 2 # This is a shorthand or shortcut for a = a ** 2 = 36.0
print(a)

# Star equals (%=) (Note: the last value of a is 36)
a %= 5 # This is a shorthand or shortcut for a = a % 5 = 1.0
print(a)

# divmod() is a built_in function
# divmod() finds simultaneously the quotient and the remainder
# 14 is divided by 6 has a quotient of 2 and a remainder of 2 as well
a, b = divmod(14, 6)
print(a, b)

# pow() is called power of number
print(pow(2, 5))

# sum() This will sum up the total value in the square parentheses
print(sum([1, 2, 3, 4, 5]))

# max() This will find the maximum value in the square parentheses
print(max([1, 2, 3, 4, 5]))

# min() This finds the minimum value in the square parentheses
print(min([1, 2, 3, 4, 5, -6]))

# round() This round the given value below to the nearest decimal value
a = 5.646772
print(round(a, 3))
b = round(a, 1)
print(a, b)

