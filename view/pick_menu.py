import pygame
import sys
from button import Button

from model.assassin import Assassin
from model.mage import Mage
from model.melee import Melee
from model.ranger import Ranger

class PickMenuState:
    def __init__(self, controller, window_width, window_height, game_mode, match_scores=None):
        self.game_mode = game_mode

        self.controller = controller
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        # Доступные герои
        self.available_heroes = [Assassin, Mage, Melee, Ranger]
        self.selected_heroes_team1 = []
        self.selected_heroes_team2 = []
        self.current_team = 1
        self.match_scores = match_scores if match_scores else [0, 0]

        # Создание кнопок для героев
        self.hero_buttons = [Button(hero.__name__, (100 + i * 150, 100), 30, "navy", hero) for i, hero in enumerate(self.available_heroes)]

        # Кнопка для завершения выбора
        self.finish_button = Button("Finish", (self.window_width // 2, self.window_height - 100), 50, "green", "finish")

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.hero_buttons:
                action = button.click(event)
                if action:
                    self.pick_hero(action)
            if self.finish_button.click(event) == "finish":
                self.finish_picking()

    def pick_hero(self, hero_class):
        if self.current_team == 1 and len(self.selected_heroes_team1) < 3:
            self.selected_heroes_team1.append(hero_class)
            self.current_team = 2
        elif self.current_team == 2 and len(self.selected_heroes_team2) < 3:
            self.selected_heroes_team2.append(hero_class)
            self.current_team = 1

        # Disable the button for the picked hero
        for button in self.hero_buttons:
            if button.feedback == hero_class:
                button.disable()

    def finish_picking(self):
        if len(self.selected_heroes_team1) == 2 and len(self.selected_heroes_team2) == 2:
            from view.gameplay_view import GameplayState
            self.controller.set_state(GameplayState(self.controller, self.window_width, self.window_height, self.selected_heroes_team1, self.selected_heroes_team2, self.game_mode, self.match_scores))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        # Отрисовка кнопок героев
        for button in self.hero_buttons:
            button.check_hover()
            button.show(screen)

        # Отрисовка кнопки завершения выбора
        self.finish_button.show(screen)

        # Отрисовка выбранных героев
        font = pygame.font.SysFont("Arial", 24)
        team1_text = font.render(f"Team 1: {[hero.__name__ for hero in self.selected_heroes_team1]}", True, pygame.Color("white"))
        team2_text = font.render(f"Team 2: {[hero.__name__ for hero in self.selected_heroes_team2]}", True, pygame.Color("white"))
        screen.blit(team1_text, (50, self.window_height - 200))
        screen.blit(team2_text, (self.window_width - 300, self.window_height - 200))

        pygame.display.flip()
