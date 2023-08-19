# CONVERTING TYPES

# 1 mile = 1.609 km
# miles = float(input('Enter distance in miles:'))
# # print(type(miles))
# # miles = float(miles)
# km = miles * 1.609
# print('Distance in km:', km)

a = 10
b = 2.5
c = '8.2'

# int => float
a_float = float(a)
print('a:', type(a))
print('a_float:', type(a_float))

# float => int
b_int = int(b)
print('b_int:', type(b_int))

# float => str
b_str = str(b)
print('b_str:', type(b_str))

# str => float
c_float = float(c)
print('c_float:', type(c_float))

# str => int
# Note: if you  want to convert a string to an int,
# you have to convert it first to a foat and then to an int.
# Of course you lose the dcimal part.
c_int = int(float(c))
print('c_int:', type(c_int))