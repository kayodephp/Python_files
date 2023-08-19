# SRING SLICING
movie = 'The Godfather'
print(movie[0:2])

# string_variable[start:stop]

print(movie[2:5])
print(movie[:2])
print(movie[4:])
print(movie[-2:])

# movie[:1] + movie[1:] is equal to movie
print(movie[:4] + movie[4:])
print(movie[3:100])

# string_variable[start:stop:stop]
print(movie[0:10:2]) # Pick the first one, then pick every second letter and stop at 10th character
print(movie[::]) # This return entire string from the beginning to the end
print(movie[::-1]) # This read and print the characters in backward / reverse


