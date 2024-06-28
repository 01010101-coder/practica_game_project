
class Hero:
    def __init__(self, x, y):
        self.hp = None
        self.damage
        self.speed
        self.attack_time
        self.range
        self.move_speed
        self.startpos = [x, y]
        self.position
        self.cooldown
        self.countdown
        self.effects
        self.stuntime
        self.stuncount
        self.poisontime
        self.poisoncount

    def attack(self):
        pass
    def cast_spell(self):
       pass

    def distance(self, enemy_pos):
        return ((self.position[0] - enemy_pos[0]) ** 2 + (self.position[1] - enemy_pos[1]) ** 2) ** 0.5

    def logic(self, ally_champ, enemy_champ):
        pass
