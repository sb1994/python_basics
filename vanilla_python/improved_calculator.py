num1 = float(input('Enter the First Number: '))
operator = input('Enter the Operator: ')
num2 = float(input('Enter the Second Number: '))


if operator == '+':
  print(num1 + num2)
elif operator == '-':
  print(num1 - num2)
elif operator == '/':
  print(num1 / num2)
elif operator == '*':
  print(num1 * num2)
else:
  print('Invalid Operator')