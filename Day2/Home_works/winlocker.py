

from tkinter import *
from tkinter import messagebox
def btn_click():
    k = ent.get()
    if k == 'СИМ СИМ АЧЫЛ!':
        messagebox.showinfo(title = 'Ура!!!', message = 'Куттуктайм! Сиздин Windows ачылды')
        root.destroy()
    else:
        message.showwarning(title = 'Неа', message = 'Пароль туура эмес!')    
def exits():
    if ent.get() != 'СИМ СИМ АЧЫЛ!':    
        message.showwarning(title = 'Неа', message = 'Пароль туура эмес!')  
root = Tk()
root.title('Сиздин Windows жабылып калды')

root.geometry('400x200')
root['bg'] = 'black'
root.protocol('WM_DELETE_WINDOW', exits)
root.resizable(width=False, height=False)
Label(root, text = 'Парольду жазыныз', font = 'Arial 25', bg = 'black', fg = 'white').pack()
ent = Entry(root, text = '', font = 'Arial 25', width = 15)
ent.pack()
Button(root, text = 'Жаздым', font = 'Arial 25', bg = 'yellow', fg = 'black', command = btn_click).pack()
root.mainloop()


