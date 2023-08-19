# This project will calculate BMI: Body Mass Index
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height: '))
bmi = weight / height ** 2

# lb or LB is in pound
# Other Cases: if you are using emprical system, just adjust the formula
# to bmi = weight(lb) / height(in) ** 2 * 703 by using LB for Weight,
# and inches for the Height and multiply the Height by 703

print('Your BMI is', format(bmi, '.2f'))