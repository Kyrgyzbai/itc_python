# 1
# bluda = {
#     'besh_barmak': 155,
#     'lagman': 135,
#     'borch': 90
# }
# bluda['besh_barmak'] = 135
# bluda.popitem()
# print(bluda)
# 2
# menus = {
#     'besh_barmak': 155,
#     'lagman': 135,
#     'drinks': ['Coca-Cola', 'Fanta', 'Sprite']
# }
# print(menus['drinks'])
# 3
# myset = {
#     'add',
#     'remove',
#     'discard',
#     'intersection',
#     'intersection_update'
#     'difference',
#     'difference_update',
#     'update',
#     'pop'
# }
# mydict = {
#     'popitem',
#     'items',
#     'keys',
#     'values',
#     'get',
#     'update'
# }
# 4
# user = {}
# for i in range(3):
#     name = input('Ваше имя: ')
#     parol = input('Ваш пароль: ')
#     user[name] = parol
# print(user)
# 5
personal = {
    'Salax': 'Футболист',
    'Хабиб': 'UFC боец',
    'Джонни Депп': 'Актер',
    'Эдвард сноуден': 'Хакер',
    'Залкарбек': 'Программист'
}

for per in personal.keys():
    print('Здравствуй, меня зовут:', per, 'я', personal[per])