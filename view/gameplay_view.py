import pygame
from model.game_model import GameModel
import sys

class GameplayState:
    def __init__(self, controller, window_width, window_height, team_1, team_2, game_mode):
        self.controller = controller
        self.model = GameModel(team_1, team_2, game_mode)
        self.view = GameView(self.model, window_width, window_height)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def update(self):
        self.model.update()

    def draw(self, screen):
        self.view.draw(screen)


class GameView:
    def __init__(self, model, window_width, window_height):
        self.model = model

        # Настройки размеров элементов в процентах
        self.arena_width_pct = 0.75
        self.arena_height_pct = 0.8
        self.icon_width_pct = 0.125
        self.score_height_pct = 0.15

        # Вычисление размеров элементов
        self.window_width = window_width
        self.window_height = window_height
        self.arena_width = int(self.window_width * self.arena_width_pct)
        self.arena_height = int(self.window_height * self.arena_height_pct)
        self.icon_width = int(self.window_width * self.icon_width_pct)
        self.score_height = int(self.window_height * self.score_height_pct)

        # Инициализация шрифта
        self.font = pygame.font.SysFont("Arial", 36)

    def draw(self, screen):
        screen.fill((200, 200, 200))  # Цвет фона

        # Отрисовка арены
        arena_x = self.icon_width
        arena_y = self.score_height
        pygame.draw.rect(screen, (255, 255, 255), (arena_x, arena_y, self.arena_width, self.arena_height))

        # Отрисовка зоны для иконок персонажей слева
        pygame.draw.rect(screen, (150, 150, 150), (0, self.score_height, self.icon_width, self.arena_height))

        # Отрисовка зоны для иконок персонажей справа
        pygame.draw.rect(screen, (150, 150, 150),
                         (self.icon_width + self.arena_width, self.score_height, self.icon_width, self.arena_height))

        # Отрисовка зоны для общего счета матча сверху
        pygame.draw.rect(screen, (100, 100, 100), (0, 0, self.window_width, self.score_height))

        # Отрисовка счета матча
        score_text = f"Team 1: {self.model.scores[0]}  -  Team 2: {self.model.scores[1]}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(self.window_width // 2, self.score_height // 2))
        screen.blit(score_surface, score_rect)

        # Отрисовка героев на арене и полосок здоровья
        for hero in self.model.heroes['team_1']:
            self.draw_hero(screen, hero, (255, abs(hero.hp), 0))

        for hero in self.model.heroes['team_2']:
            self.draw_hero(screen, hero, (0, abs(hero.hp), 255))

        pygame.display.flip()

    def draw_hero(self, screen, hero, color):
        # Отрисовка героя
        pygame.draw.circle(screen, color, hero.position, 20)
        # Отрисовка полоски здоровья
        self.draw_health_bar(screen, hero)

    def draw_health_bar(self, screen, hero):
        bar_width = 40
        bar_height = 5
        # Определение длины полоски здоровья в зависимости от текущего здоровья
        health_ratio = hero.hp / hero.max_hp  # Предполагая, что максимальное здоровье героя 100
        current_bar_width = int(bar_width * health_ratio)
        # Определение позиции полоски здоровья
        bar_x = hero.position[0] - bar_width // 2
        bar_y = hero.position[1] - 30  # Над героем
        # Отрисовка фона полоски здоровья (серый цвет)
        pygame.draw.rect(screen, (128, 128, 128), (bar_x, bar_y, bar_width, bar_height))
        # Отрисовка текущего состояния здоровья (зелёный цвет)
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, current_bar_width, bar_height))
