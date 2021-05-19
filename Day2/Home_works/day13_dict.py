# Автосалон Bootcamp
# car1 = {
#     'model': 'Honda Fit 2',
#     'year': '2008',
#     'vol': 1.6,
#     'color': 'silver',
#     'price': 5500.0,
#     'max_speed': 260
# }

# car2 = {
#     'model': 'Mercedes SLG 63',
#     'year': '2016',
#     'vol': 4.0,
#     'color': 'black',
#     'price': 142000.0,
#     'max_speed': 350
# }
# car3 = {
#     'model': 'Matiz 2',
#     'year': '2008',
#     'vol': 1.4,
#     'color': 'blue',
#     'price': 3500.0,
#     'max_speed': 180
# }
# print('Добро пожаловать в Автосалон Bootcamp.')
# print('Машины в наличии: ')
# print('1: ', car1['model'])
# print('2: ', car2['model'])
# print('3: ', car3['model'])
# select_car = int(input('Какую машину выбрать: '))


# if select_car == 1:
   
#     print('Поздравляем, ваша мащина: ')
#     print('model:', car1['model'])
#     print('year:', car1['year'])
#     print('vol:', car1['vol'])
#     print('color:', car1['color'])
#     print('price:', car1['price'])
#     print('max_speed:', car1['max_speed'])
#     print(car_key,':', car1[car_key])


# if select_car == 2:
#     print('Поздравляем, ваша мащина: ')
#     print('model:', car2['model'])
#     print('year:', car2['year'])
#     print('vol:', car2['vol'])
#     print('color:', car2['color'])
#     print('price:', car2['price'])
#     print('max_speed:', car2['max_speed'])

# if select_car == 3:
#     print('Поздравляем, ваша мащина: ')
#     print('model:', car3['model'])
#     print('year:', car3['year'])
#     print('vol:', car3['vol'])
#     print('color:', car3['color'])
#     print('price:', car3['price'])
#     print('max_speed:', car3['max_speed'])


######### AMANTUR ###############
# amantur = {
#     'fio: ' : 'Торогулов Амантур',
#     'pol: ' : 'Мужчина',
#     'age: ' : 13,
#     'ves: ' : 31,
#     'rost: ' : 162,
#     'adress: ' : 'Ош',
#     'birthday: ' : '2 сентября, 2007 г. ',
#     'school; ' : 'ITC BootCamp',
# }

# # amantur['IQ: '] = 110
# # amantur.clear()
# # amantur.keys()

# # print(amantur.keys())
# # print(amantur['fio: '])
# # print(amantur.values())
# print(amantur.get('fio: '))

#   car_key = input('Какую характеристику хотите посмотреть?: ')
#     if car1.get(car_key) != None:
#         print(car_key,':', car1[car_key])
#     else:
#         print('Мындай характеристика жок')


######## АШ СУББОТАГА #############

mesto = {
    'Дарханга',
    'Манас-Атага',
    'Палван атага',
    'Караванга',
    'копчулук эмне десе ошол жакка',
    'офиске'
}

foods = {
    'аш',
    'пицца',
    'ачуу эт',
    'пирожок',
    'лагман',
    'мясной рулет',
    'ташкентский аш',
    'тибон',
}


start = 'start'
#input('Баштоо учун "start" деп жазыныз: ')
# Наугад кайсыл жерде отурабыз жана кандай тамак жейбиз чыгарып бериш керек.

mesto1 = mesto.pop()
foods1 = foods.pop()

if start == start:
    print('Биз келе жаткан суббота коллектив менен', mesto1, 'барабыз жана', foods1, 'жейбиз.')