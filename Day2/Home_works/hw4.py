# #Problem1:
#      # Дан произвольный список. my_list = [1, 5, 8, 11, 55, 62, 78, 86, 91]
#      # Представьте его в обратном порядке.
     
# my_list = [1, 5, 8, 11, 55, 62, 78, 86, 91]
# print(my_list[::-1])

# # #Problem2:
# #       # Напишите программу, которая принимает список и меняет местами его первый и последний элемент. Т.е получить из old_list => new_list
# #       # old_list = [5, 6, 8, 99, 4, 62, 73]    => new_list = [73, 6, 8, 99, 4, 62, 5]
# old_list = [5, 6, 8, 99, 4, 62, 73]
# # new_list = [73, 6, 8, 99, 4, 62, 5]
# old_list[0]=old_list[-1]
# print(old_list)
      
      #Problem6:
      # Создать пустой лист. Добавить в него сначала ваше имя, год рождения, любимый язык программирования.
      
# name = input('Ваше имя:')
# bornYear = input('Год рождения:')
# language = input('Любимый язык программирования:')

# print(name)
# print(bornYear)
# print(language)

#Problem4:
      # Напишите программу, которая удаляет последний элемент из массива: 

# lst = [9, 5, 7, 4, 2, 6, 8, 1]
# lst.pop(7)
# print(lst)

# #Problem5:
#       # Напишите программу, которая считает количество похожих элементов, в этом случае наш элемент "5" из массива: 

# lst = [9, 5, 7, 5, 2, 6, 5, 1, 9, 54]
# print(lst.count(5))

#Problem7:
      # Удалить из листа [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] все чётные индексы до 10.
