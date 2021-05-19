# Задача 1.
# создайте файл friends.txt
# напишите туда имена своих друзей и их возраст с помощью open('friends.txt', 'w')
# Например содержимое файла должен быть:
    # Руслан,26
    # Кадыр,23
    # Ерлан,22



# myfile = open("./Home_works/friends.txt", "w")
# text = myfile.writelines("")

# print(text)

# friendslist = [
# 'Руслан, 26 \n',
# 'Кадыр, 23 \n',
# 'Эрдан, 22 \n'
# ]

# # myfile = open("./Home_works/friends.txt", "a")
# # text = myfile.writelines(friendslist)

# print(text)

# for i in friendslist:
#     myfile.write(i)


# =================================================================

# Задание 2
# Создайте функцию splitFio(fio) которое разделяет имя и фамилию
# Например:
    # Ввод: splitFio('Асан уулу Рулсан')
    # Вывод: Имя: Руслан Фамилия: Асан уулу
    
    # Ввод: splitFio('Тургунбаева Айсулуу')
    # Вывод: Имя: Айсулуу Фамилия: Тургунбаева

# def main():


#     splitFio = input('Как Ваше ФИО? ')
#     name_list = splitFio.split()

#     print(name_list)

#     first = name_list[0]
#     second = name_list[1]
#     last = name_list[2]

#     print("Фамилия: ", first.capitalize(),'\n Имя: ', second.capitalize(),'\n Отчество:  ', last.capitalize()) 


# main()

# =================================================================

# Задание 3
# создайте файл tasks.txt и напишите туда разные уравнения
# создайте функцию run_task() которое открывает файл tasks.txt и выполняет уравнения
# Например содержимое файла tasks.txt:
# 20+99
# 199/3
# 200**5
# 500+1976
# При запуске функции run_task()
# Вывод:
#   20+99=119
#   199/3=106
#   200**5=320000000000
#   500+1976=2476

# =================================================================

# file = open("./Home_works/tasks.txt", "r")
# print(file.read())

# text = file.writelines("")

# print(text)


# run_task = [
# 20+99,
# 199/3,
# 200**5,
# 500+1976,
# ]

# print(run_task)

# file = open("./Home_works/tasks.txt", "a")
# text = file.writelines(str(run_task))

# print(run_task)

# for i in run_task:
#     file.write(str(i))


# ===========================================


task_file = open('./Home_works/tasks.txt', 'r')
task_lists = task_file.readlines()

for task in task_lists:
    try: # коркунучтуу аварийный жерлерде кодлонушубуз керек
        t = task.strip()
        print(t, '=', eval(t))
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except:
        print('Выражение неправилен!')