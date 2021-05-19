import crypt


class Client:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.set_password(password)
    
    def set_password(self, password):
        self.__password = password
        if len(password) < 8:
            print('слабый пароль')
        else:
            self. __password = password

    def get_password(self):
        return 'шифрованный'
    
    def raw_password(self):
        print('никому не рассказывайте пароль')
        return self.__password
        



# Интернет магазин bootcamp
# наш клиент
turgun = Client('Тургунбай', 'turgun', '1994' )
# новый пароль
print(turgun.set_password('1234567891234'))
# вызываем пароль
print(turgun.get_password())
# сырой пароль
print(turgun.raw_password())