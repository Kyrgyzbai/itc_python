# 1.
# Создай Class Teacher
# свойство:
# name - имя учителя
# age - возраст учителя 
# predmet - имя предмет (по какому предмету препод-т)
# создайте функции:
# to_teach(self): - должна показывать по какому предмету обучает
    
# На основое Class Teacher создай обьекты учителей по:
# Физике  
# Биологии
# Математики

# =============================================================================

# class Teacher:
#     def __init__(self, name, age, predmet):
#         self.name = name
#         self.age = age
#         self.predmet = predmet

    

#     def to_teach(self):
#         print('Привет, меня зовут', self.name, 'и я учу детей', self.predmet[0: 9].lower()+'e')

# teacher = Teacher('Айнура', 40, 'Математика')
# teacher.to_teach()

# =================================================================

# 2.
# Создай Обьект Plane реализуй его свойство и умение летать

# class Plane:
#     def __init__(self, ability):
#         self.ability = ability

#     def to_fly(self):
#         print('могу', self.ability.lower())

# plane = Plane('Летать')
# plane.to_fly()

# ======================================================================


# 3.
# Создай Обьект Hacker реализуй все его свойство и умение 
# Характеристики:
# уровень - уровень хакера
# навыки - какими навыками он обладает
# возраст - возраст хакера
# пол

# Что он может делать ?
# Например: взломать почту, взлом сайта, взлом сети



# class Hacker:
#     def __init__(self, level, ability, age):
#         self.level = level
#         self.ability = ability
#         self.age = age
        

    

#     def to_hack(self):
#         print('Привет, мой', self.level, 'и я могу' , self.ability, 'и мой возраст всего', self.age, 'лет. Ха-ха-ха')

# hacker = Hacker('уровень хакера', 'взломать почту, взлом сайта, взлом сети', 23)
# hacker.to_hack()

# ======================================================================



# class Teacher:
#     def __init__(self, name, age, predmet):
#         self.name = name
#         self.age = age
#         self.predmet = predmet

    

#     def to_teach(self):
#         print('Привет, меня зовут', self.name, 'и я учу детей', self.predmet[0: 9].lower()+'e')

# teacher = Teacher('Айнура', 40, 'Математика')
# teacher.to_teach()

# teacher1 = Teacher('Айнура', 40, 'физика')
# teacher1.to_teach()

# teacher2 = Teacher('Айнура', 40, 'биологии')
# teacher2.to_teach()