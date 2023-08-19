# #CONDITIONAL STATEMENTS
# balance = 100
# price =50
# if balance >= price:
# answer = input('Do you want to continue? Enter yes or no:')
# answer = answer.lower() # This eliminate either the user type in UPPERCASE/LOWERCASE
#     if answer == 'yes':
#         print('We\'ll move on.')
#     elif answer == 'no':
#         print('We\'ll stop.')
#     else:
#         print('Invalid answer.')
#     balance_price = balance - price
#     new_balance = balance_price
#     print(f'You can book the flight and your new balance will be {new_balance}.')
# else:
#     print(f'Insufficient funds! Please deposit {price - balance}')

x = 10
if x <= 10:
    print('x less than or equal to 10.')
elif x == 10:
    print('x is equal to 10.')
else: print('x greater than 10.')