
class Hero:
    def __init__(self, x, y):
        self.name = None
        self.hp = None
        self.damage = None

        self.move_speed = None

        self.allys_position = []
        self.enemy_position = []

        self.position = [x, y]
    def attack(self):
        return "attack"

    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y

    def cast_spell(self):
        return "cast_spell"

    def logic(self):
        if self.position[0] < 600 and self.position[1] < 500:
            self.move(10, 20)
            print(self.allys_position)
