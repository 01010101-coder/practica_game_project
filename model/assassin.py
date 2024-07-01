import time
import pygame
from model.hero import Hero

class Assassin(Hero):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.load_sprite('view/sprites/assasin.png')
        self.max_hp = 70
        self.hp = 70
        self.damage = 8
        self.speed = 10  # in ticks
        self.attack_time = 0
        self.range = 15
        self.move_speed = 1
        self.startpos = [x, y]
        self.position = [x, y]
        self.cooldown = 5
        self.spell_time = time.time()

        self.team = team

        self.attack_cooldown = 1.0  # Attack every 1 second
        self.last_attack_time = time.time()

        # effects and variables
        self.effects = []
        self.stuntime = 0
        self.stuncount = 0
        self.poisontime = 0
        self.poisoncount = 0
        self.spell = "dash"

        self.kills = 0
        self.deaths = 0

    def __name__(self):
        return "Assasin"

    def load_sprite(self, image_path):
        self.sprite = pygame.image.load(image_path)
        self.sprite = pygame.transform.scale(self.sprite, (30, 30))  # Скалирование спрайта до нужного размера


    def cast_spell(self, nearest_enemy, enemy_champ):
        second_closest = [100000, 100000]
        for enemy in enemy_champ:
            if enemy != nearest_enemy:
                if self.distance(enemy.position) < self.distance(second_closest):
                    second_closest = enemy.position
        self.position = [second_closest[0] - 10, second_closest[1] - 10]

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
        nearest_enemy = min(enemy_champ, key=lambda enemy: self.distance(enemy.position))
        if time.time() - self.spell_time >= self.cooldown:
            self.cast_spell(nearest_enemy, enemy_champ)
            self.spell_time = time.time()
        # attack or move
        if self.distance(nearest_enemy.position) > self.range:
            self.move(nearest_enemy.position)
        else:
            self.attack(nearest_enemy)