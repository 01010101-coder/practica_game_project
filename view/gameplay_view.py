import pygame
import sys
from model.game_model import GameModel
from view.pick_menu import PickMenuState
from view.gameover_view import GameOverState

class GameplayState:
    def __init__(self, controller, window_width, window_height, team_1, team_2, game_mode, match_scores=None):
        self.controller = controller
        self.model = GameModel(team_1, team_2, game_mode)
        if match_scores:
            self.model.match_scores = match_scores
        self.view = GameView(self.model, window_width, window_height)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def update(self):
        match_over = self.model.update()
        if match_over:
            if self.model.is_series_over():
                self.controller.set_state(GameOverState(self.controller, self.model.match_scores, self.view.window_width, self.view.window_height))
            else:
                self.controller.set_state(PickMenuState(self.controller, self.view.window_width, self.view.window_height, self.model.game_mode, self.model.match_scores))

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
        self.small_font = pygame.font.SysFont("Arial", 18)  # Уменьшенный шрифт

    def draw(self, screen):
        screen.fill((200, 200, 200))  # Цвет фона

        # Отрисовка зоны для общего счета матча сверху
        pygame.draw.rect(screen, (100, 100, 100), (0, 0, self.window_width, self.score_height))

        # Отрисовка счета матчей
        match_score_text = f"Matches - Team 1: {self.model.match_scores[0]}  -  Team 2: {self.model.match_scores[1]}"
        match_score_surface = self.font.render(match_score_text, True, (255, 255, 255))
        match_score_rect = match_score_surface.get_rect(center=(self.window_width // 2, self.score_height // 3))
        screen.blit(match_score_surface, match_score_rect)

        # Отрисовка счета матча
        score_text = f"Team 1: {self.model.scores[0]}  -  Team 2: {self.model.scores[1]}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(self.window_width // 2, self.score_height // 1.5))
        screen.blit(score_surface, score_rect)

        # Отрисовка арены
        arena_x = self.icon_width
        arena_y = self.score_height
        pygame.draw.rect(screen, (255, 255, 255), (arena_x, arena_y, self.arena_width, self.arena_height))

        # Отрисовка зоны для иконок персонажей слева
        pygame.draw.rect(screen, (150, 150, 150), (0, self.score_height, self.icon_width, self.arena_height))

        # Отрисовка зоны для иконок персонажей справа
        pygame.draw.rect(screen, (150, 150, 150), (self.icon_width + self.arena_width, self.score_height, self.icon_width, self.arena_height))

        # Отрисовка героев на арене и их полосок HP
        for hero in self.model.heroes['team_1']:
            pygame.draw.circle(screen, (255, abs(hero.hp), 0), hero.position, 20)
            self.draw_health_bar(screen, hero)
        for hero in self.model.heroes['team_2']:
            pygame.draw.circle(screen, (0, abs(hero.hp), 255), hero.position, 20)
            self.draw_health_bar(screen, hero)

        # Отрисовка героев и статистики по бокам
        self.draw_hero_stats(screen, self.model.heroes['team_1'], 0, self.score_height)
        self.draw_hero_stats(screen, self.model.heroes['team_2'], self.icon_width + self.arena_width, self.score_height)

        pygame.display.flip()

    def draw_health_bar(self, screen, hero):
        bar_width = 40
        bar_height = 5
        bar_x = hero.position[0] - bar_width // 2
        bar_y = hero.position[1] - 30  # Расположение полоски HP над героем
        health_ratio = hero.hp / hero.max_hp
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))  # Фон полоски (красный)
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))  # Полоска здоровья (зеленый)

    def draw_hero_stats(self, screen, heroes, start_x, start_y):
        for i, hero in enumerate(heroes):
            name_text = type(hero).__name__
            stats_text = f"Kills: {hero.kills}, Deaths: {hero.deaths}"
            name_surface = self.small_font.render(name_text, True, (255, 255, 255))
            stats_surface = self.small_font.render(stats_text, True, (255, 255, 255))
            screen.blit(name_surface, (start_x + 5, start_y + i * 60))  # Немного отступаем от края
            screen.blit(stats_surface, (start_x + 5, start_y + i * 60 + 20))  # Немного отступаем от края и делаем перенос строки
