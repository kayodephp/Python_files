# Arithmetic Operators

# +
print(5 + 5)
# -
print(3-9)
# /
print(8 / 4)

# // its an integer division which returns an integer value
print(11 // 2)

# *
print(5 * 4)

# **
print(2 ** 100)

# % is called Modulus that returns its remainder
print(8 % 5)
print(14 % 4)

# If you use an integer to multiply a float number, the result is float
print(4 * 5.0)

# Order of Operations (Operator Precedence)
# Exponentiation (**) come first
# Multiplication (*) and Division (/) follows
# Addition (+) and Subtraction (-)
print(2 + 4 * 2 ** 3) # The answer will be 34

# Lets change the Order of Precedences by using parentheses
# This will make Addition to be Evaluated first by using Parentheses
print((2 + 4) * 2 ** 3) # The answer will be 48

# If you a large number as 1000000000
print(1_000_000_000)
print(1000 == 1_000)
