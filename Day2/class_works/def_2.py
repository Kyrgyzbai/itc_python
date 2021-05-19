
# # Телефон номерин текшере турган программа
# def check_phone_number(check_phone):
#     if zero == check_phone[0] and len(check_phone) == 10:
#         print('Идет вызов на ', check_phone)
#     else:
#         print("Вы неправильно ввели номер!")
    
    
# print('Пример: 0772551144')
# phone = input('Введите номер телефона: ')
# zero = '0'

# check_phone_number(phone)


operators = {
    'megacom': [
        '0558',
        '0551',
        '0555',
        '0557',
        '0553',
        '0996',
        '0550',
    ],
    'beeline': [
        '0770',
        '0777',
        '0778',
        '0776',
        '0771',
        '0222',
    ],
    'Ошка': [
        '0700',
        '0999',
        '0701',
        '0702'
    ],
    
    'gorod': [
        '3222'
    ]
}
def check_phone_number(nomer):
    if len(nomer) == 10 and nomer[0] == '0':
        print('Номер телефона правильный')
        code = nomer[0:4]
        if code in operators['Ошка']:
            print('Ваш оператор Ошка')
        elif code in operators['megacom']:
            print('Ваш оператор MegaCom')
        elif code in operators['beeline']:
            print('Ваш оператор Beeline')
        code = nomer[0:5]
        if code in operators['gorod']:
            print('Ваш оператор Gorod')
    else:
        print('Вы ввели неправильный номер')
phone = input('Введите номер телефона: ')
# phone2 = input('Введите номер телефона: ')
print('Ваш номер: ', phone)
check_phone_number(phone)
# print()
# check_phone_number(phone2)