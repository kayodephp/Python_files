# THE WALRUS OPERATOR

# name := expression
# print(x := 2 + 5)
# print(f'x is {x}')
#
# value = input('Enter something: ')
# while value != '':
#     print(f'You entered: {value}')
#     value = input('Enter something: ')

# This lines of codes is the same as the above code
# while(value := input('Enter something: ')) != '':
#     print(f'You entered: {value}')

# This another one different to the above
# data = input('Enter your name: ')
# if len(data) > 0:
#     print(f'Your name has {len(data)} characters.')
# else:
#     print('your name can not be empty.')


# This code is a better version of the above
data = input('Enter your name: ')
if (n := len(data)) > 0:
    print(f'Your name has {n} characters.')
else:
    print('your name can not be empty.')