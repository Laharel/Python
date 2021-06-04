class Fighter:
    def __init__(self, name, hp = 10, str =20, vit =5) :
        self.name = name
        self.health = hp
        self.hp = self.health*10
        self.strength = str
        self.vitality = vit
        self.defense = self.vitality*3
        self.damage = self.strength*2

    def attack(self, other):
        damage = self.damage - other.defense
        other.hp -= damage
        print(f"{other.name} has taken {damage} damage \n {other.name}'s hp = {other.hp}")
    
    def battle(self, other):
        while (self.hp>0 and other.hp>0):
            self.attack(other)
            if (other.hp>0):
                other.attack(self)

class Thief:
    def __init__(self) -> None:
        pass

Jack = Fighter("Jack")
Happy = Fighter("happy", hp = 12)
Jack.battle(Happy)