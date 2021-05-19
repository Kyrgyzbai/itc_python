story_count = {'сто': 100,
               'девяносто': 90,
               'двенадцать': 12,
               'пять': 5}
select = input('Пиши: ')
print(story_count.get(select))
