
# глобальная область видимости
san = 96 

def myprint(san): 
    # локальная область видимости
    print(san)

myprint(19)
print(san)