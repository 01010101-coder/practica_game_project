import time
import pygame
from model.hero import Hero

class Mage(Hero):
    def __init__(self, x, y):
        self.name = type
        self.hp = 70
        self.damage = 15
        self.speed = 50 # in ticks
        self.attack_time = 0
        self.range = 100
        self.move_speed = 1
        self.startpos = [x, y]
        self.position = self.startpos
        self.cooldown = 6
        self.spell_time = time.time()
        # effects and variables
        self.effects = []
        self.stuntime = 0
        self.stuncount = 0
        self.poisontime = 0
        self.poisoncount = 0
        self.spell = "stun"

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
        current_time = pygame.time.get_ticks()
        if current_time - self.attack_time >= self.speed:
            enemy.hp -= self.damage
            self.attack_time = current_time

    def cast_spell(self, enemy):
        enemy.effects.add("stun")
        enemy.poisoncount = 2
        enemy.poisontime = time.time()

    def logic(self, ally_champ, enemy_champ, score):
        if not enemy_champ:
            return
        # death
        if self.hp <= 0:
            score += 1
            self.effects = []
            self.hp = 100
            self.position = self.startpos
            return
            # stunned
        if "stun" in self.effects:
            if self.stuncount <= 0:
                self.effects.remove("stun")
            else:
                self.stuncount -= time.time() - self.stuntime
                self.stuntime = time.time()
                return
            # poisoned
        if "poison" in self.effects:
            if self.poisoncount <= 0:
                self.effects.remove("poison")
                return
            else:
                self.poisoncount -= time.time() - self.poisontime
                self.hp -= time.time() - self.poisontime
                self.poisontime = time.time()
        # spellcast
        nearest_enemy = min(enemy_champ, key=lambda enemy: self.distance(enemy.position))
        if time.time() - self.spell_time >= self.cooldown:
            self.cast_spell(nearest_enemy)
            self.stuntime = time.time()
        # attack or move
        if self.distance(nearest_enemy.position) > self.range:
            self.move(nearest_enemy.position)
        elif self.distance(nearest_enemy.position) < self.range:
            reverse_enemy = [nearest_enemy.position[0] * -1, nearest_enemy.position[1] * -1]
            self.move(reverse_enemy)
            self.attack(nearest_enemy)
        else:
            self.attack(nearest_enemy)