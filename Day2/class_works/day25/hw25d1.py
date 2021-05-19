# Problem1

# Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. 
# По умолчанию name = Aman, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, 
# setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, 
# метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения 
# данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, 
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.


# # ==========================================================================
# class Student:
#     def __init__(self):
#         self.name = 'Aman'     
#         self.age = 18          
#         self.group_number = '10 A'
 
# #  получаем старых параметров =================================
#     def get_name(self):
#         return self.name
 
#     def get_age(self):
#         return self.age
    
#     def get_group_number(self):
#         return self.group_number
    
# # установка новых параметров =================================

#     def set_name(self, name):
#         self.name = name

#     def set_age(self, age):
#         if age in range(1, 100):
#             self.age = age
#         else:
#             print("Недопустимый возраст")     
         
#     def set_group_number(self, group_number):
#         self.group_number = group_number
 
# #  Покажи мне ====================================================
#     def show_me_info(self):
#         print("Имя:", self.name, "\nВозраст:", self.age, '\nНомер группы:', self.group_number, '\n=================================')
         
# aman = Student()
 
# aman.show_me_info()
# aman.set_name('Esen')
# aman.set_age(20)
# aman.set_group_number('11B')
# aman.show_me_info()



# ====================================================================

# Problem2

# Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение, 
# multiplication — умножение, division — деление, subtraction — вычитание. 
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

# ========================================================================

# print("Введите 2 числа: ")
# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# class Math:
#     def addition(self, a, b):
#         print(a, '+', b, '=', a + b)
    
#     def multiplication (self, a, b):
#         print(a, '*', b, '=', a * b)

#     def division (self, a, b):
#         print(a, '/', b, '=', a / b)

#     def subtraction (self, a, b):
#         print(a, '-', b, '=', a - b)

# # =================================

# math = Math()
# math.addition(a, b)
# math.multiplication(a, b)
# math.division(a, b)
# math.subtraction(a, b)


# ==============================================================================

# Problem3

# Напишите программу с классом Car. Создайте конструктор класса Car. 
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
# Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. 
# Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.


# class Car:
#     def __init__(self, color, mytype, year):
#         self.color = color
#         self.type = mytype
#         self.year = year

#     def start_engine(self):
#         print('Автомобиль заведен')
    
#     def stop_engine(self):
#         print('Автомобиль заглушен')

#     def set_mytype(self, mytype):
#         self.mytype = mytype

#     def set_year(self, year):
#         self.year = year

#     def set_color(self, color):
#         self.color = color


#     def show_info(self):
#         print("Цвет автомобиля: ", self.color, "\nГод выпуска: ", self.year, '\nТип: ', self.mytype, '\n=================================')


# car = Car(year = 2020, color = '', mytype = '')

# car.set_color('Белый')
# car.set_year(2000)
# car.set_mytype('Седан')
# car.show_info()

# =========================================================================


class Car:
    # def (self, color, mytype, year):
    #     self.color = color
    #     self.type = mytype
    #     self.year = year

    def start_engine(self):
        print('Автомобиль заведен')
    
    def stop_engine(self):
        print('Автомобиль заглушен')

    def set_mytype(self, mytype):
        self.mytype = mytype

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color


    def show_info(self):
        print("Цвет автомобиля: ", self.color, "\nГод выпуска: ", self.year, '\nТип: ', self.mytype, '\n=================================')


car = Car()

car.set_color('Белый')
car.set_year(2000)
car.set_mytype('Седан')
car.show_info()
car.stop_engine()
car.start_engine()