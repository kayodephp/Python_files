# STRING CONCATENATION AND REPETITION
# + => the concatenation operator

movie = 'The Godfather '
director = 'Francis Ford Coppola'
movie_and_director = movie + director
print(movie_and_director)
print(movie + ' was director by ' + director)

language = 'Python'
version = 3.11
print(language + str(version))

# * => the repetition operator
print(movie * 5)
print('#' * 50)
price = '10.5 '
print(price * 5)

# To multiply it by 5, you have to first convert it to a float
print(float(price) * 5)