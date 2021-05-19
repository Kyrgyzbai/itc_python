# # words = 'когда интернет не работает перезагрузи компьютер. Интернет тогда заработает'
# # # # суйломдон кандайдыр бир созду таап алуу туурасында
# # print("интер" in words) # 1 способ

# # if 'интернет' in words: # бул экинчи способ
# #     print('есть')

# products = ['sugar','melon']
# # print([products.count('sugar')]) индекс боюнча иштейт
# if 'sug' in products:
#     print('sugar have')
# else:
#     print('sugar dont have')
    
    
# ########## SETS & DICTIONARY ##########

# # множество {} менен жазылат

# names = {
#     'zalkar',
#     'zalkar',
#     'beka',
#     'beka',
#     'tom'
# }

# print(names) # бул жерде кайталанган дубликаттын бироосун гана чыгарат калганын очуруп коет, рандомдо чыгар, изменяемый


# emails = [
#     'bek',
#     'zak',
#     'bek',
#     'zak',
#     'erl',
#     'ama',
# ]

# emails = set(emails) # бул жерде жогорудагы список [] ну  множество {} озгортуп коет 

# for email in emails:
#     print('на почту', email, 'отправить письмо') 
   
   
 
# friends = {
#     'bektur',
#     'zalkar',
#     'bektur',
#     'zalkar',
#     'erlan',
#     'amamtur',
# }
# print(friends)

# products = {
#     'sugar',
#     'tea',
#     'water',
#     'melon'
# }

# print('before ', products)
# products.remove('melon')
# print('afer ',  products)
# # newproduct = ''

# for i in range(3):
#     mewproduct = input('add new product: ')
#     products.add(newproduct) добавляет новый продукт к продуктам

# print(products)


#############################

# products = {
#     'sugar',
#     'tea',
#     'water',
#     'melon'
# }

# newproducts = {
#     'meat',
#     'carrot'
#}
# print('before ', products)
# products.clear() очищает
# print('afer ',  products)

#############################

# print('before ', products) эки множествону кошуп коет
# products.update(newproducts)
# print('afer ',  products)

# company1 = {'apple', 'sony', 'lg'}
# company2 = {'apple', 'daewoo', 'mercedes'}

# print(company1.difference(company2)) #  находит разницу

################################


# intersection = company1.intersection(company2) # эки коптукто дагы окшош нерселерди чыгарып берет.

# print(intersection)

# company1.intersection_update(company2) # эки озгормону салыштырып калганын очуруп сал
# print(company1)

# company1 = {
#     'apple', 'sony', 'lg'
# }
# # company1.pop() рандомно бироосун очуруп салат
# company1.pop()
# print(company1)

# users = {
#     'Zalkar',
#     'Bekzat',
#     'Max',
#     'Man',
#     'Jax',
#     'Sam',
#     'Aibek',
#     'Nana',
# }

# users = set()
# user = ''
# lotnew = int(input('Канча орун берели?: '))
# for i in range(lotnew):
#     user = input('Катышуучулардын аттарын жазыныз: ')
#     users.add(user)

# for i in range(lotnew):
#     print(i+1,'орун', users.pop())

###### парольдордун базасын тузуу ######

# users = set()
# user = ''
# lotnew = int(input('Канча орун берели?: '))
# for i in range(lotnew):
#     user = input('Катышуучулардын аттарын жазыныз: ')
#     users.add(user)

# for i in range(lotnew):
#     print(i+1,'орун', users.pop())
    
pwrds = set()
pwrd = ''
numpwrd = int(input('Канча турлуу пароль киргизесиз: '))

for i in range(numpwrd):
    pwrd = int(input('Пароль киргизиниз: '))
    pwrds.add(pwrd)

for i in range(numpwrd):
    print(i+1, '- пароль: ', pwrds.pop())