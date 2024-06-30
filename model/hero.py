import time

class Hero:
    def __init__(self, x, y, team):
        pass

    def move(self, target_position):
        if self.position[0] < target_position[0]:
            self.position[0] += self.move_speed
        elif self.position[0] > target_position[0]:
            self.position[0] -= self.move_speed

        if self.position[1] < target_position[1]:
            self.position[1] += self.move_speed
        elif self.position[1] > target_position[1]:
            self.position[1] -= self.move_speed


    def attack(self, enemy):
        current_time = time.time()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            enemy.hp -= self.damage
            self.last_attack_time = current_time
            print(f"Attacked {enemy.__name__} for {self.damage} damage. Enemy HP: {enemy.hp}")

    def distance(self, enemy_pos):
        return ((self.position[0] - enemy_pos[0]) ** 2 + (self.position[1] - enemy_pos[1]) ** 2) ** 0.5
