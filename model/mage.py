import time
import pygame
from model.hero import Hero

class Mage(Hero):
    def __init__(self, x, y, team):
        self.max_hp = 70
        self.hp = 70
        self.damage = 5
        self.speed = 50 # in ticks
        self.attack_time = 0
        self.range = 55
        self.move_speed = 1
        self.startpos = [x, y]
        self.position = [x, y]
        self.cooldown = 5
        self.spell_time = time.time()

        self.team = team

        self.attack_cooldown = 1.5  # Attack every 1 second
        self.last_attack_time = time.time()

        # effects and variables
        self.effects = []
        self.stuntime = 0
        self.stuncount = 0
        self.poisontime = 0
        self.poisoncount = 0
        self.spell = "stun"

    def __name__(self):
        return "Mage"

    def cast_spell(self, enemy):
        enemy.effects.append("stun")
        enemy.stuncount = 2
        enemy.stuntime = time.time()

    def logic(self, model, ally_champ, enemy_champ):
        if not enemy_champ:
            return

        # death
        if self.hp <= 0:
            model.scores[0] += 1
            self.effects = []
            self.hp = 100
            self.position = self.startpos.copy()
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
        else:
            self.attack(nearest_enemy)