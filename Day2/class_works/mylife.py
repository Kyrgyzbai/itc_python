year = input('Азыр канчанчы жыл?: ')
year1 = input('Канчанчы жылы туулгансыз?: ')
year2 = 32
month = year2 * 12
day = month * 30
hour = day * 24
minute = hour * 60
second = minute * 60
year1 = int(year1)
year = int(year)


print('Сиз',year - year1, 'жаштасыз')
print('Сиз ' , month , 'ай жашадыныз')
print('Сиз ' , day , 'кун жашадыныз')
print('Сиз ' , hour , 'саат жашадыныз')
print('Сиз ' , minute , 'минута жашадыныз')
print('Сиз ' , second , 'секунда жашадыныз')