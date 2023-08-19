# INTRO TO PYTHON STRINGS
# A string is an ordered sequence of UTF-8 enclosed characters.

my_str1 = 'I learn Python'
my_str2 = "I learn Python"

print(my_str1)

# Hi there! I'm Kayode
print('Hi there! I\'m Kayode')
print("Hi there! I'm Kayode")

# Multiple line String
message = 'He said: "Go for it"'
print(type(message))

languages = """I like Python
Golang
and
Solidity.
"""
print(languages)

# Another way to declare a multi line string is to use single or double quotes and add a backslash n or t at the end of each line.
# Backslash N is called an escape sequence and is an ASCII code for a new line that is being created at that point in the string.
my_languages = 'I like Python\nGolang\nand\nSolidity.'
print(my_languages)

# Finally, I want to mention the special character backslash, which is also called the Escape Character.
# A single backslash is used in representing certain whitespace characters.
# For example, backslash TX is a tab and the backslash N is a new line.
print('a\tb\tc\td\te')

# The backslash character is also used to cancel the special meaning of the character that follows.
# For example, if you want to print backslash n literally you write backslash backslash n.
# The first backslash will cancel the special meaning of backslash n it will print out backslash n literally.
# Or if you want to print quotes, you can use back slashes as well.

print('\\n')

print('He says: "I\'m 20"')
print('\\ is a special character in Python.')
