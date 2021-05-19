class Animal:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Lion(Animal):
    def to_attack(self):
        print(self.name,':','Roar', 'Tackle')
        print('health: ', self.hp)

class KingKong(Animal):
    def to_attack(self):
        print(self.name,':','Hyper Punch','Tackle')
        print('health: ', self.hp)


class Krokodile(Animal):
    def to_attack(self):
        print(self.name,':','Earthquake','Tackle')
        print('health: ', self.hp)
animal  = Animal('leo',55)

leo = Lion(
    name='leo',
    hp=130
)
kingkong = KingKong(
    name='kingkong',
    hp=630

)    
krok = Krokodile(
    name='krok',
    hp=55
)


kingkong.to_attack()
leo.to_attack()
krok.to_attack()