# ---------------------------------------------------------------------------------------#
# Задача 1:
# У нас есть словарь фруктов fruits.

# Спроси у клиента 3 вида фруктов
# Выведи на экран их картинки
# Например:
#    Ввод: алма
#    Ввод: дарбыз
#    Ввод: дыня  
#    Вывод: 🍎, 🍉 🍈

# ---------------------------------------------------------------------------------------#

# fruits = {
#    'алма':'🍎',
#    'дарбыз':'🍉',
#    'дыня':'🍈',
#    'помидор': '🍅',
#    'кулпунай': '🍓',
#    'банан': '🍌'
# }

# select = input('Танданыз: ')
# print('Сиз тандадыныз: ', fruits.get(select))


# ---------------------------------------------------------------------------------------#
# Задача 2:
# Времена года
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

# Ввод: 6
# Вывод: Лето

# Ввод: 3
# Вывод: Весна
# # ---------------------------------------------------------------------------------------#

# season = {
#    1:'кыш',
#    2:"кыш",
#    3:"жаз",
#    4:'жаз',
#    5:"жаз",
#    6:"жай",
#    7:'жай',
#    8:"жай",
#    9:"куз",
#    10:'куз',
#    11:"куз",
#    12:"кыш",
# }

# month = int(input('Айды киргизиниз: '))

# print("Бул ай", season.get(month), 'мезгили')
       
    
# ---------------------------------------------------------------------------------------#
# Задача 3.
# Написать функцию deposit(money, year) который прибавляет, к деньгам money, 15% от money.
# 1 аргумент это сумма деген которые мы хотим вложит в депозит
# 2 аргумент срок депозита
# Функция должна вычислить депозит на year лет
# Вызов: deposit(50000, 2)
# Вывод: За 2 года деньги увеличились на 65000
# ---------------------------------------------------------------------------------------#

# def deposit(money, year):
#     depo_st = (money * 0.15) * year
#     result = money + depo_st
#     print('За {0} года деньги увеличились на {1}'.format(year, result))
 
# mon = int(input('Количество денег на депозите: '))
# year = int(input('На сколько лет: '))
# deposit(mon, year)


# ---------------------------------------------------------------------------------------#
# Задача 4.
# Есть список a = [1, 1, 2, 3, 5, 9, 8, 13, 21, 34, 55, 89, 75].
# Выведите все элементы, которые меньше 9.
# ---------------------------------------------------------------------------------------#


# ---------------------------------------------------------------------------------------#
# Задача 5.
# lst = [100, 29, 33, 44, 32, 65, 345, 99, 900, 32]
# Выведите первый и последний элемент списка.
# ---------------------------------------------------------------------------------------#