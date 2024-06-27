class Hero:
    def __init__(self, x, y):
        self.name = "Hero"
        self.hp = 100
        self.damage = 10
        self.range = 1
        self.move_speed = 5
        self.position = [x, y]
        self.effects = []

    def attack(self):
        return "attack"

    def move(self, target_position):
        if self.position[0] < target_position[0]:
            self.position[0] += self.move_speed
        elif self.position[0] > target_position[0]:
            self.position[0] -= self.move_speed

        if self.position[1] < target_position[1]:
            self.position[1] += self.move_speed
        elif self.position[1] > target_position[1]:
            self.position[1] -= self.move_speed

    def cast_spell(self):
        return "cast_spell"

    def distance(self, enemy_pos):
        return ((self.position[0] - enemy_pos[0]) ** 2 + (self.position[1] - enemy_pos[1]) ** 2) ** 0.5

    def logic(self, ally_champ, enemy_champ):
        if not enemy_champ:
            return
        nearest_enemy = min(enemy_champ, key=lambda enemy: self.distance(enemy.position))
        self.move(nearest_enemy.position)
