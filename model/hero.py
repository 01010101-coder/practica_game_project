import time
import pygame

class Hero:
    def __init__(self, x, y, team):
        self.position = [x, y]
        self.sprite = None
        self.description = "A generic hero"
        self.sprite_path = "view/sprites/assassin.png"

    def load_sprite(self, image_path):
        self.sprite = pygame.image.load(image_path)
        self.sprite = pygame.transform.scale(self.sprite, (60, 60))  # Скалирование спрайта до нужного размера

    def draw(self, screen):
        if self.sprite:
            screen.blit(self.sprite, self.position)

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
            if enemy.hp <= 0:
                self.kills += 1

    def distance(self, enemy_pos):
        return ((self.position[0] - enemy_pos[0]) ** 2 + (self.position[1] - enemy_pos[1]) ** 2) ** 0.5
