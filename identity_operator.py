# Identity Operators#: "is" and "is not"

a, b = 3, 4
print(a is b)

# Lets talk about Mutability and Immutability
# The value of a mutable variable can be changed after it has been created, but the value of an immutable
# variable can't be changed.
# If we try to change the value of an immutable variable, python will create a new variable that stores

# Immutable types: int, float, str, tuple, frozenset
# Mutable types: list, set, dict

# Example
print(id(a))
a += 3
print(a)
print(id(a))

# Lets see an example with a Mutable data type
# List below
numbers = [1, 2, 3]
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers)) # This has same address as line 22 because its Mutable and can be changed

# Now, lets create a copy of the list using the copy method
nums = numbers.copy()
print(nums == numbers) # This will give true because it has same content

print(nums is numbers) # This returns false because they save in diffefernt addresses
