# PROJECT: PASSWORD GENERATOR

# 1. Never share your password
# 2. Use a strong password
# 3. Don't reuse your passwords
# 4. Use 2 factor authentication for all your sites i.e. 2FA

import  random
import string
chars = string.ascii_letters + string.digits + string.punctuation
print(random.choice(chars))
# length = 12
length = int(input('Password length: '))
password = ''

for _ in range(length):
    c = random.choice(chars)
    password += c

print(f'Your random password is: {password}')