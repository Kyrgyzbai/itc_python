# # Динамические получает параметры

# # def sample(*args):
# #     sum = 0
# #     for a in args:
# #         sum = sum + a
# #     print(sum)

# # sample(10, 20, 80)

# def sample(**kwargs):
#     print(kwargs['name'])
#     print(kwargs['model'])
#     print(kwargs['weight'])
#     print(kwargs['god'])
#     print(kwargs['price'])

# sample(
#     name = 'Toyota', 
#     model = 'Prius',
#     weight = '2400 kg',
#     god = '2012 year',
#     price = '2021$'
# )


def my_computer(**kwargs):
    print(kwargs['processor'])
    print(kwargs['ghz'])
    print(kwargs['core'])
    print(kwargs['harddisk'])
    print(kwargs['videocard'])


my_computer(
    processor = 'intel Core I9 90900K',
    ghz = '8.6 ghz',
    core = '36',
    harddisk = '500 tb',
    videocard = 'GTX 9080 Ti',
    ram = '128gb',
    model = 'Asus Rog'
)