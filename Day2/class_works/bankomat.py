# balance = 10000
# moneywithdraw = ''
# pword = ''
# mypass = 2021


# cardnumber = input('Введите номер вашей карты:')
# pword = int(input('Введите пинкод: '))

# if pword == mypass:
#     print('навашем балансе' , balance , '$')
# else:
#     print('неверный пин!')
#     pword = int(input('Введите пинкод еще раз: '))
#     print('Вы неправильно ввели пин 2 раза. Пока!')
#     quit()
    

# moneywithdraw = int(input('Скролько денег хотите снять?'))
# balance = balance - moneywithdraw
# print('Вы снимали ' , moneywithdraw ,'$')
# print('Остаток на вашем балансе' , balance )

balance = 10000 # баланс
correct_pin = 2021 # правильный пин

print('Здравствуйте! Вас приветствует банкомат банка Demir Bank') # приветствие
pincode = int(input('Введите ПИН КОД: ')) # введем пин код
if pincode == correct_pin: # если пин код введен правильно то:
    # списки операции
    print('1. Проверка баланса')
    print('2. Снятие денег')
    print('3. Изменить ПИН КОД')
    # выбор операции
    operation = int(input('Выберите операцию: '))
    if operation == 1:
        # проверяет остаток на балансе
        print('На Вашем балансе ',balance,' сом')
        # снимаем денежных средств
    elif operation == 2:
        get_money = int(input('Сколько денег хотите снять? '))
        # в балансе оставляем 100 сои
        if get_money > (balance - 100):
            print('У Вас недостаточно денежных средств')
            quit()
        balance = balance - get_money
        print('Вы снимали',get_money, 'сом. Ваш остаток на балансе ',balance, 'сом')
    # меняем ПИН КОД
    elif operation == 3:
        correct_pin = int(input('Введите новый ПИН КОД:'))
        print('ПИН КОД был изменён')
        # проверяем пин код
        pincode = int(input('Введите новый ПИН КОД для проверки: '))
        if pincode == correct_pin:
            print('Новый ПИН КОД верный')
        else:
            print('Новый ПИН КОД не верный')
           
else:
    print('Вы ввели не правильный ПИН КОД')
    quit()