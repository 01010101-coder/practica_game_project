import time
import pygame
from model.hero import Hero

class Healer(Hero):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.load_sprite('view/sprites/healer.png')
        self.max_hp = 70
        self.hp = 70
        self.heal_amount = 10
        self.damage = 2
        self.speed = 50
        self.attack_time = 0
        self.range = 125
        self.move_speed = 1
        self.startpos = [x, y]
        self.position = [x, y]
        self.cooldown = 3
        self.spell_time = time.time()

        self.team = team

        self.description = "A generic hero"
        self.sprite_path = "view/sprites/healer.png"

        self.attack_cooldown = 1.5  # Attack every 1.5 seconds
        self.last_attack_time = time.time()

        # effects and variables
        self.effects = []
        self.stuntime = 0
        self.stuncount = 0
        self.poisontime = 0
        self.poisoncount = 0
        self.spell = "heal"

        self.kills = 0
        self.deaths = 0

    def __name__(self):
        return "Healer"

    def cast_spell(self, ally_champ):
        if ally_champ:
            lowest_hp_ally = min(ally_champ, key=lambda ally: ally.hp)
            lowest_hp_ally.hp = lowest_hp_ally.hp + self.heal_amount

    def logic(self, model, ally_champ, enemy_champ):
        if not enemy_champ:
            return

        # death
        if self.hp <= 0:
            if self.team == 1:
                model.scores[0] += 1
            else:
                model.scores[1] += 1
            self.effects = []
            self.hp = self.max_hp
            self.position = self.startpos.copy()
            self.deaths += 1
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
        if time.time() - self.spell_time >= self.cooldown:
            self.cast_spell(ally_champ)
            self.spell_time = time.time()

        # attack or move
        nearest_enemy = min(enemy_champ, key=lambda enemy: self.distance(enemy.position))
        if self.distance(nearest_enemy.position) > self.range:
            self.move(nearest_enemy.position)
        else:
            self.attack(nearest_enemy)
