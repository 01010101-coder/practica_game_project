import pygame
from model.game_model import GameModel
import sys


class GameplayState:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.model = GameModel()
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

        # Отрисовка героев на арене
        for hero in self.model.heroes['team_1']:
            pygame.draw.circle(screen, (hero.hp * 2, 0, 0), hero.position, 20)
        for hero in self.model.heroes['team_2']:
            pygame.draw.circle(screen, (0, 0, hero.hp * 2), hero.position, 20)
        pygame.display.flip()
