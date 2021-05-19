

# g = int(
#     input('Сан бериниз: ')
# )

# factorial = 1
# for i in range(2, g+1):
#     factorial *= i

# print(factorial)

# # print(1*2*3*4*5*6*7*8*9)



# def factorial(g):
#     if g == 0:
#         return 1
#     return factorial(g-1) * g
 
 
# print(factorial())

# def progress(num):
#     geo = 1
#     for i in range(1, num + 1):
#         geo = geo * i
#         text = text + '{} *'.format(i)
#     print('Ответ: ', text, geo)

# # g = int(
# #     input('Бир сан териниз: ')
# # )


# g2 = int(
#     input('Бир сан териниз: ')
# )

# # progress(g)
# progress(g2)

# def progress(num):
#     geo = 1
#     text = ''
#     for i in range(1, num + 1):
#         geo = geo * i
#         if i == num:
#             text = text + '{} = '.format(i)
#         else:
#             text = text + '{} * '.format(i)
#     print('Ответ:', text, geo)
# g = int(
#     input('Сан бериниз 1: ')
# )
# # g2 = int(
# #     input('Сан бериниз 2: ')
# # )
# progress(g)
# # progress(g2)


# Уйдо факториал эмес суммасын чыгара турган кыл



# def progress(num):
#     geo = 0
#     text = ''
#     for i in range(1, num + 1):
#         geo = geo + i
#         if i == num:
#             text = text + '{} = '.format(i)
#         else:
#             text = text + '{} + '.format(i)
#     print('Ответ:', text, geo)
# g = int(
#     input('Сан бериниз 1: ')
# )
# # g2 = int(
# #     input('Сан бериниз 2: ')
# # )
# progress(g)
# # progress(g2)

n = input()
 
suma = 0
mult = 1
 
for digit in n:
    if digit.isdigit():
        suma += int(digit)
        mult *= int(digit)
 
print("Сумма:", suma)
print("Произведение:", mult)