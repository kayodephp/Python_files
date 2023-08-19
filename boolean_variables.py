# TRUTHINESS OF OBJECTS

# result = ''
# if result:
#     print('result is not empty.')
# else:
#     print('result is empty.')

result = ''
if bool(result):
    print('result is not empty.')
else:
    print('result is empty.')

var1 = '' # You can test this line with => '', [], 'ss', [1, 2]
if var1:
    print('var1 truthy value is True.')
else:
    print('var1 truthy value is False.')