# RANGES

r = range(2, 10) # You can specify to print each after 3 step using r = range(2, 10, 3) else it will print a list of integers from 2 to 9 one by one.
print(type(r))
print(list(r))

print(list(range(0, 11, 2))) # This will move in 2 steps
print(list(range(0, 40, 7)))
s = sum(range(0, 1001))
print(s)

# Summary
# 1. range(stop)
print(list(range(10))) # range(0, 10, 1)

# 2. range(start, stop)
print(list(range(3, 9))) # This is the same as range(3, 9, 1)

# 3. range(start, stop, step)
print(list(range(5, 100, 13)))

print(list(range(-20, 10, 4)))
print(list(range(10, -2, -3)))

# The RANGES are used in FOR LOOP