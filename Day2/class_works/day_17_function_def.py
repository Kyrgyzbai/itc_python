# функция это блок операторов которые можно вызывать где угодно

# def sum(num1, num2):
#     print('----')
#     print('Сумма: {}'.format(num1 + num2))
#     print('----')
    
# def minus(num1, num2):
#     print('----')
#     print('Сумма: {}'.format(num1 - num2))
#     print('----')



# san1 = int(input('Биринчи санды киргизиниз: '))
# san2 = int(input('Экинчи санды киргизиниз: '))

# sum(san1, san2)
# minus(san1, san2)

# 1-вариант
# def salam_en(): 
#     print('Hi! How are you?')
#     print('Lets learn Python')

# def salam_kg():
#     print('Салам! Акыбал кандай?')
#     print('Кел Python уйронобуз')

# # 2=вариант
# def salamdash(lang):
#     if lang == 'en':
#         print('Hello Hi How are You')
#         print('Maybe go to learn Python')
#     elif lang == 'kg':
#         print('Ассалоому Алейкум. Иштер кандай ?')
#         print('Python уйронгону кеттикби')
#     elif lang == 'ru':
#         print('Добрый вечер')
#         print('Поехали бухат')
# l = input('Кайсы тилде саламдашайын: ')
# salamdash(l)

def calculator(san1, san2, suff):
    if suff == '*':
        print('Жообу: ', san1 * san2)
    elif suff == '/':
        print('Жообу: ',san1 / san2)
    elif suff == '+':
        print('Жообу: ',san1 + san2)
    elif suff == '-':
        print('Жообу: ',san1 - san2)        
        
# calculator(5, 5, '*')

n1 = int(input('биринчи сан:'))
n2 = int(input('экинчи сан:'))
s = input('Эмне кылыш керек:')

calculator(n1, n2, s)