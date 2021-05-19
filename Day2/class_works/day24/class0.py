# # Объекты (классы)
# # Ылдыйда биз статический класс тузуп алабыз

# # class Tiger:
# #     name = 'Sherkhan'
# #     weight = 400
# #     age = 5
# #     color = 'yellow'
# #     speed = 50
# #     power = 99

# # tigr = Tiger()

# # tigr2 = Tiger()
# # tigr2.name = 'Mursik'
# # tigr2.weight = 300


# # print('Имя тигра: ', tigr.name)
# # print('Масса тигра: ', tigr.weight)
# # print('Возраст тигра: ', tigr.age)
# # print('Цвет тигра: ', tigr.color)
# # print('Скорость тигра: ', tigr.speed)
# # print('Сила тигра: ', tigr.power)



# # print('Имя тигра: ', tigr2.name)
# # print('Масса тигра: ', tigr2.weight)
# # print('Возраст тигра: ', tigr2.age)
# # print('Цвет тигра: ', tigr2.color)
# # print('Скорость тигра: ', tigr2.speed)
# # print('Сила тигра: ', tigr2.power)


# # =======================================================

# # class Human:
# #     name = ''
# #     sex = ''
# #     color = ''
# #     weight = ''
# #     age = ''
# #     def to_walk(self):
# #         print(self.name,'Басып кетип  жатам')
# #     def to_speak(self, word, word2):
# #         print(self, "говорит", word, word2)

# # human = Human()

# # human.name = 'Bekzat'
# # human.sex = 'Male'
# # human.color = 'white'
# # human.weight = '77 kg'
# # age = 32

# # human.to_speak(
# #     'Salam kanday',
# #     'Jakshy ozung?'
# # )


# # =================================================================

# # class Car:
# #     rasxod_100 = 12
# #     ai92 = 50
# #     ai95 = 55

# #     def __init__(self, name, year, color, vol):
# #         self.name = name
# #         self.year = year
# #         self.color = color
# #         self.vol = vol
    
# #     def get_vol(self):
# #         print('Мой объем: ', self.vol)
    
# #     def get_rasxod(self, km):
# #         r = (km / 100) * self,rasxod_100
# #         print('Расход на', km, r)

# #     def get_rasxod_price(self, km, ai92):
# #         r = (km / 100) * self,rasxod_100_price
# #         print('Расход на', km*ai92)




# # mycar = Car( 
# #     name = 'Toyota 100', 
# #     year = 2001, 
# #     color = 'green', 
# #     vol = 4.7)

# # print(mycar.name)
# # print(mycar.year)
# # print(mycar.color)
# # print(mycar.vol)



# # mycar.get_vol()
# # mycar.get_rasxod(40)
# # mycar.get_rasxod_price()

# # =================================================================
# # # ОБьект Машина

# ai_92 = 49.50
# ai_95 = 51.50
# class Car:
#     rasxod_100 = 12
#     def __init___(self, name, year, color, volume):
#         self.name = name
#         self.year = year
#         self.color = color
#         self.volume = volume
    
#     def get_volume(self):
#         print('Мой обьем:', self.volume)

#     def get_rasxod(self, km):
#         r = (km / 100) * self.rasxod_100
#         return r

#     def get_rasxod_price(self, km):
#         r = self.get_rasxod(km)
#         print('92 На', km,'km', r * ai_92, 'som')
#         print('95 На', km,'km', r * ai_95, 'som')

# mycar = Car(
#     name = 'Matiz 1', 
#     year = 2000,
#     color = 'Белый',
#     volume = 3.5
# )

# mycar.get_volume()
# mycar.get_rasxod(145)
# mycar.get_rasxod_price(145)


# =================================================================================

# class Animal:
#     def __init__(self, **kwargs):
#         self.name = kwargs['name']
#         self.type = kwargs['type']
#         self.speed = kwargs['speed']

#     def get_speed(self):
#         print('Бегает {} км в час'.format(self.speed))
    
#     def get_full_time(self, km):
#         print(km / self.speed)

# name = input('Введите имя животного: ')

# leopard = Animal(
#     name = name,
#     type = 'Кошачий',
#     speed = 90
# )

# leopard.get_speed()
# leopard.get_full_time(80)


# # =======================================================

# Написать характеристики своего компьютера

# class PC:
#     def __init__(self, **kwargs):
#         self.processor = kwargs.pop('processor')

# mypc = PC(
#     processor = "Intel Core i9 - 90900K"
# )


# # ============================================================================
