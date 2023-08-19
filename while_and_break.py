# WHILE AND BREAK

# while True:
#     guess = int(input('Enter your lucky number [1-10]:'))
#     if guess == 7:
#         print('You won!')
#         break
#     print(f'{guess} was not a lucky number!')

a = int(input('Enter number: '))
while a > 1:
    b = a // 2 # This returns the quotient a // 2. i.e: quotient of 12 // 3 is 4
    while b > 1:
        if a % b == 0: # Testing if result of a % b is not a prime number
            break
        b -= 1
    else: # belongs to inner while
        print(f'{a} is prime')
    a -= 1