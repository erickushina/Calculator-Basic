def calculator ():
  if mul == 'yes':
    total = num * num2
    return total
  elif subtr == 'yes':
    total = num - num2
    return total
  elif divide == 'yes':
    total = num // num2
    return total

def choose_operator():
  if mul == 'yes':
    op = 'To Multiply'
    return op
  elif  subtr == 'yes':
    op = '"To Subtract"'
    return op
  elif divide == 'yes':
    op = '"To Divide"'
    return op

def signal_operator():
  if mul == 'yes':
    sig = 'x'
    return sig
  elif subtr == 'yes':
    sig = '-'
    return sig
  elif divide == 'yes':
    sig = '/'
    return sig

print('WELCOME TO MY CALCULATOR!!\n')
print('Do you Want?: ')
mul = input('Multiplication?: ').lower()
subtr = input('Minus: ' ).lower()
divide = input('Divition?: ').lower()
print('\n')


operator = mul, subtr, divide

choose = choose_operator()
print(f'OK. You chose {choose}.')
print('Please. Enter the numbers you want to calculate: ')
num = int(input('Number 1: '))
num2 = int(input('Number 2: '))
print('\n')

result = calculator()

signal_op = signal_operator()

print(f'{num} {signal_op} {num2} = {result}')
print(f'The result is  : {result}')