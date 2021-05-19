# a = 7
# b = 0
# if b == 0:
#     print('ообв b нолго барабар')
#     print('yes')
# else:
#     print('канчага барабар билбеймин')
    
######

# a = 7
# b = 5
# if b == a:
#     print('ообв b a барабар')
#     print('yes')
# else:
#     print('канчага барабар билбеймин')
    
    # #####


# # форма авторизации для сайта

# # Registration form
# newUsername = input('New username: ')
# newPassword = input('New password')
    
# # authentication form
# myUsername = input('Enter your username: ')
# myPassword = input('Enter password: ')

# if myPassword == newPassword and myUsername == newUsername:
#     print('access granted')
# else:
#     print('access denied')


# Calculator

# Entering value

number1 = int(input('enter first number: '))
symbol = input('what you want?: ')
number2 = int(input('enter second nunber: '))
result = ''

# here are logics

# plus
if symbol == '+':
    result = number1 + number2
    
# minus
if symbol == "-":
    result = number1 - number2

# divide
if symbol == '*':
    result = number1 * number2
    
# multiple

if symbol == '*':
    result = number1 * number2


elif symbol =='/':
    if number2 != 0:
        
        result = number1 / number2
    else:
        print('ERROR!')
        
# degree
if symbol == "**":
    result = number1 ** number2

# here is result

print(number1, symbol, number2, '=', result)

