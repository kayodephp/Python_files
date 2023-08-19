# Floating Point Arithmetic: Issues and Limitations

print(0.125 == 1/10 + 2/100 + 5/1000)

print(format(1/3, '.20f'))

print(format(1/10, '.20f'))
print(format(0.1, '.20f'))

print(format(0.125, '.50f'))

a = 0.1 * 3
b = 0.3
print(a == b)

print(format(a, '.25f'))

# to solve the problems of floating
# We make use of isclose() function math module
# You can define module as a collection of variables, functions and classes that
# are already defined in Python
# We just import the module and X functionality
from  math import isclose
# isclose()
x = 0.00000001 # For small numbers, we make use of absolute tolerance
y = 0.00000002
print(x == y)

print(isclose(x, y, abs_tol=0.01)) # abs_tol means absolute tolerance

a = 999999999.01 # For large numbers, we make use of reletive tolerance
b = 999999999.02
print(isclose(a, b, rel_tol=0.01))

a = 3.4
b = 2.3
print(a + b) # 5.7

print(format(a, '.25f'))
print(format(b, '.25f'))