# Онлайн покупка через aliexpress
# Покупка Ноутбука Acer Predator 3500$
# AliExpress принимает только Visa и PayPal и SberPay
# # Mastercard и Elcard не поддерживает

# print('Чтобы купить Acer Predator за 3500$: ')
# sposob = input('введит способ оплаты: ')
# if sposob == 'Mastercard':
#     print('Извините мы не поддерживаем MasterCard')
# elif sposob == 'Elcard':
#     print('Извините мы не поддерживаем Elcard')
# # cridcard = input('введите номер вашей карты: ')

# visa = 'Visa'
# paypal = 'PayPal'
# mastercard = 'MasterCard'
# elcard = 'Elcard'
# sberpay = 'SberPay'
# sposoboplaty = 'способ оплаты'
# creditcard = ''
# sdacha = ''
# nbprice = 3500

# print('Вас приветствует AliExpress!')

# tovar = input('Что хотели бы покупать?: ')
# print('Отличный выбор!', tovar, 'стоит' , nbprice, '$') 
# sposob = input('''Каким способом хотите оплатить? 
# Мы принимаем Visa, PayPal, SberPay:''')

# if sposob == mastercard:
#     print('Извините мы не поддерживаем карты MascterCard')
# elif sposob == elcard:
#     print('Извините мы не поддерживаем карты Elcard')
# elif sposob == visa or sposob == paypal():
#    creditcard = input('Введите номер вашей карты: ')
#    if len(creditcard) > 4 or len(creditcard) < 4:
#        input('Ваш товар стоит', nbprice , '$')
#        balance = int(input('Введите сумму оплаты: '))
       
##########################
       
#        if balance < nbprice:
#            print('Недостаточно средств')
#        elif balance > nbprice: 
#            print('Спасибо за покупку! Ваша сдача')
           
# else: print('Такой вид карты не поддерживается!')

#############################


# Онлайн покупка через aliexpress
# Покупка Ноутбука Acer Predator 3500$
# AliExpress принимает только Visa и PayPal и SberPay
# Mastercard и Elcard не поддерживает
predator_sena = 3500 # Цена: Acer Predator 
balance = 3200 # Биздин баштапкы баланс
card_len = 16
print('Чтобы купить Acer Predator за 3500$: ')
sposob = (input('введит способ оплаты: ')).lower()
if sposob == 'mastercard':
    print('Извините мы не поддерживаем MasterCard')
elif sposob == 'elcard':
    print('Извините мы не поддерживаем Elcard')
elif sposob == 'visa' or sposob == 'paypal':
    creditcard = input('введите номер вашей карты: ')
    if len(creditcard) > 4 or len(creditcard) < 4:
        print('Некорректный номер карты ??')
        quit()
    if predator_sena > balance:
        print('У вас недостаточно средтсв не хватает для покупки')
    else:
        print('Вы можете совершить покупку.')
else:
    print('Такой вид карты не поддерживается')