from tkinter import *
from random import randint

root = Tk()
root.title('Чай-пай генератор')
root.geometry('400x100')

# Тамактар
mesto = [
    'Дарханга',
    'Манас-Атага',
    'Палван атага',
    'Караванга',
    'копчулук эмне десе ошол жакка',
    'офиске'
]

foods = {
    'аш',
    'пицца',
    'ачуу эт',
    'пирожок',
    'лагман',
    'мясной рулет',
    'ташкентский аш',
    'тибон',
}

# Конвертируем на set
mesto_set = set(mesto)

# # # Конвертируем на списки
unique_mesto = list(mesto_set)

# # # Создаем list size
our_number = len(unique_mesto) - 1

# # # создаем рандомное число
rando = randint(0, our_number)

def pick():
    return

    winnerLabel = Label(root, text=len, font=('Arial', 16))
    winnerLabel.pack(pady=14)

topLabel = Label(root, text=unique_mesto[rando], font=('Arial', 20))
topLabel.pack(pady=20)



# winButton = Button(root, text='Чыгарып бер', font=('Arial', 20), command=pick)
# winButton.pack(pady=20)

root.mainloop()

