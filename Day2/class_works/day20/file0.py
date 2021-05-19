# f = open("./class_works/day20/sample.txt", "wb")
# text = f.writelines("")

# print(text)

# fruits = [
# 'Алма\n',
# 'Орук\n',
# 'Дарбыз\n', 
# 'Коон\n',
# '\n'
# ]

# f = open("./class_works/day20/sample.txt", "a")
# text = f.writelines(fruits)

# print(text)

# for i in fruits:
#     f.write(i)


# ------------------------



# #Читать
# akipress = open('https://www.tazabek.kg/news:1700965?from=portal&place=last&b=1', 'r')
# akipress_text = akipress.read()

# file = open('sample.txt', 'w')
# # Записать на файл sample.txt
# file.write(akipress_text)



#Читать
akipress = open('https://ibooks.oshsu.kg/', 'r')
akipress_text = akipress.read()

file = open('sample.txt', 'w')
# Записать на файл sample.txt
file.write(akipress_text)

