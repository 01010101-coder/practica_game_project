import time
import pygame
from model.hero import Hero

class Barbarian(Hero):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.load_sprite('view/sprites/barbarian.png')
        self.max_hp = 100
        self.hp = 100
        self.damage = 8
        self.default_speed = 50
        self.speed = self.default_speed
        self.attack_time = 0
        self.range = 30
        self.move_speed = 1
        self.startpos = [x, y]
        self.position = [x, y]
        self.cooldown = 5
        self.spell_time = time.time()

        self.description = "A generic hero"
        self.sprite_path = "view/sprites/barbarian.png"

        self.team = team

        self.attack_cooldown = 1.0  # Attack every 1 second
        self.last_attack_time = time.time()

        # effects and variables
        self.effects = []
        self.stuntime = 0
        self.stuncount = 0
        self.poisontime = 0
        self.poisoncount = 0
        self.spell = "rage"

        self.kills = 0
        self.deaths = 0

    def __name__(self):
        return "Barbarian"

    def cast_spell(self):
        pass  # Barbarian does not have a special spell, rage is passive

    def attack(self, enemy):
        current_time = time.time()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            enemy.hp -= self.damage
            self.last_attack_time = current_time
            self.increase_attack_speed()
            if enemy.hp <= 0:
                self.kills += 1

    def increase_attack_speed(self):
        self.attack_cooldown *= 0.9  # Increases attack speed by reducing cooldown

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
            self.attack_cooldown = 1.0  # Reset attack cooldown to default
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
        # attack or move
        nearest_enemy = min(enemy_champ, key=lambda enemy: self.distance(enemy.position))
        if self.distance(nearest_enemy.position) > self.range:
            self.move(nearest_enemy.position)
        else:
            self.attack(nearest_enemy)
