class Persone:

    def __init__(self, hp, power, xp):
        self.hp = hp
        self.power = power
        self.xp = xp

    def hp_izm(self, izm):
        self.hp += izm
        print(f'Ваше здоровье = {self.hp}')
        if self.hp <= 0:
            print("DEAD")

    def xp_izmn(self, izmn):
        self.xp += izmn
        print(f'Ваш навык = {self.xp}')

    def power_iz(self, iz):
        self.power += iz
        print(f'Ваша сила = {self.power}')

    def hp_pos(self):
        print(self.hp)

    def power_pos(self):
        print(self.power)

    def xp_pos(self):
        print(self.xp)
