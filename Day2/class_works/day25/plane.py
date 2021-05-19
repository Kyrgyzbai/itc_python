class Plane:
    def init(self, name, speed):
        self.name = name
        self.speed = speed

    def to_fly(self):
        print(self.name, 'Летает на скорости: ', self.speed)
    
    def get_wing_metr(self):
        print('Есть два крылья')


class Boeing(Plane): 
    def to_fly(self):
        print(self.name, 'Пасажирский самалет летает на скорости: ', self.speed)


me_plane = Plane( 
    name = 'Кукурузник', 
    speed = 350
)
b747 = Boeing(
    name = 'Boeing 747', 
    speed = 750
)

me_plane.to_fly()
me_plane.get_wing_metr()
b747.to_fly()
b747.get_wing_metr()