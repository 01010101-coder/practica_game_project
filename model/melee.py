import time
import pygame
from model.hero import Hero

clock = pygame.time.Clock()
class Melee(Hero):
    def __init__(self, x, y, team):
        self.max_hp = 120
        self.hp = 120
        self.damage = 10
        self.speed = 30
        self.attack_time = 0
        self.range = 15
        self.move_speed = 1
        self.startpos = [x, y]
        self.position = [x, y]
        self.cooldown = 4
        self.spell_time = time.time()

        self.team = team

        self.attack_cooldown = 1.0  # Attack every 1 second
        self.last_attack_time = time.time()

        #effects and variables
        self.effects = []
        self.stuntime = 0
        self.stuncount = 0
        self.poisontime = 0
        self.poisoncount = 0
        self.spell = "splash"

    def __name__(self):
        return "Melee"

    def cast_spell(self, enemy_champ):
        for enemy in enemy_champ:
            if self.distance(enemy.position) <= self.range * 2:
                self.attack(enemy)

    def logic(self, model, ally_champ, enemy_champ):
        if not enemy_champ:
            return
        #death
        if self.hp <= 0:
            model.scores[0] += 1
            self.effects = []
            self.hp = 100
            self.position = self.startpos.copy()
            return
        #stunned
        if "stun" in self.effects:
            print(self.stuncount, time.time(), self.stuntime)
            if self.stuncount <= 0:
                self.effects.remove("stun")
            else:
                self.stuncount -= time.time() - self.stuntime
                self.stuntime = time.time()
                return
        #poisoned
        if "poison" in self.effects:
            if self.poisoncount <= 0:
                self.effects.remove("poison")
                return
            else:
                self.poisoncount -= time.time() - self.poisontime
                self.hp -= time.time() - self.poisontime
                self.poisontime = time.time()
        #spellcast
        if time.time() - self.spell_time >= self.cooldown:
            self.cast_spell(enemy_champ)
            self.spell_time = time.time()
        #attack or move
        nearest_enemy = min(enemy_champ, key=lambda enemy: self.distance(enemy.position))
        if self.distance(nearest_enemy.position) > self.range:
            self.move(nearest_enemy.position)
        else:
            self.attack(nearest_enemy)
