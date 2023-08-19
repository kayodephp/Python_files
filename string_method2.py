# STRING METHODS
my_str = 'I learn Python Programming.'

# Lets learn about most IMPORTANT STRING METHODS in PYTHON
# 1. str.upper()
print(my_str.upper())

# 2. str.lower()
print(my_str.lower())

# 3. str.strip(). The eliminate all white spaces from the beginning and the end of the string
ip = '  192.168.0.1'
ip = ip.strip()
print(ip)

value = '$$200$$$$'
print(value.strip('$'))

# 4. str.replace()
new_value = value.replace('$', '£')
print(new_value)

# 5. str.count()
txt = 'I learn Python, Python is cool!'
n = txt.count('Python')
print(n)

txt1 = 'I learn PytHon, PythoN is cool!'
n1 = txt1.lower().count('python')
print(n1)

txt2 = 'I le arn Pyth   on, Python is c\nool!'
n2 = txt2.count('Python')
print(n2)

print(txt.count('y'))

# 6. str.split()
my_list = txt.split()
print(my_list)

my_list2 = txt2.split()
print(my_list2)

print('10.1.2.3'.split('.'))

# 7. str.join()
ip = '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = '.'.join(ip_list)
print(ip_str)

ip_str = ','.join(ip_list)
print(ip_str)

ip_str = '-'.join(ip_list)
print(ip_str)

ip_str = 'xxx'.join(ip_list)
print(ip_str)

# 8. str.find()
my_str = 'I learn Python Programming.'
print(my_str.find('Python')) # This will find Python at index 8

print(my_str.find('Pyxthon')) # This return -1 because it does not exist

# in => This will help you check if Python is part of the string my_str
# This return True because Python is part of the string
print('Python' in my_str)

# This will help you check if Goland is part of the string my_str
# This return False because Goland is not part of the string
print('Goland' in my_str)

# not in
print('Goland' not in my_str)