#Problem1:
    # Дана строка: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    # Ваша задача вывести на экран
    # сколько символов содержит данная строка

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. '''
print(text) 
print(len(text))

#Problem2:

z = 'z'
x = 'x'
c = 'c'
print(z*1+x*5+c*9)

 # Получить из text - text2 т.е. текст без пробела т.е. у вас должно получиться 'Loremipsumdolorsitamet,consecteturadipiscingelit,seddoeiusmodtemporincididuntutlaboreetdoloremagnaaliqua'
  
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
text2 = "Loremipsumdolorsitamet,consecteturadipiscingelit,seddoeiusmodtemporincididuntutlaboreetdoloremagnaaliqua"

print(text.replace(' ',''))

#Problem4:
    #  Получить из modified - original:
    

modified = '''исследователи ESET с()()бщили/ 
чт() в наст()ящее время активн()сть xDSpy прекратилась/ 
и пр()из()шл() эт() п()сле предупреждения/ ()публик()ванн()г() бел()русским cert в феврале текущег() г()да! 
П() сути/ т()гда эксперты ()бнаружили ()дну из вред()н()сных кампаний хакер()в/ к()т()рая и была детальн() ()писана в д()кументе! 
именн() инф()рмация бел()русск()г() cert стала ()тправн()й т()чк()й для начала расслед()вания eset и п()м()гла аналитикам ()бнаружить пр()шлые ()перации XDSpy!
'''
print(modified.replace('()','o'))

numbers = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100
    # Ваша задача вывести на экран:
    # 	- количество чисел в списке.
    # 	- получить диапазон от 30 до 60 
    # 	- получить обратный (перевернутый) диапазон от 20 до 50.
    
print(numbers)
print(len(numbers))
print(numbers[29:60])

#Problem6:
  # Дан кортеж: zoo = ('python', 'elephant', 'penguin')
  # Ваша задача вывести на экран количество животных в кортеже zoo
  
  
zoo = ('python', 'elephant', 'penguin')

print(len(zoo))

#Problem7:
    # Найдите способ вывода следующей строки без пробелов:
test = 't e s t'
print(test.replace(' ', ''))
 
 #Problem8:
#     #Расшифруйте строку ‘NATSZYGRYK’ с помощью Python.

word = 'NATSZYGRYK'
print(word[::-1])

#Problem9:
    # Напишите программу, которая вернет текст с большой буквой т.е. у вас должно получиться:
republic = 'кыргызская республика'
print(republic.title())
