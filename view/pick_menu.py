import pygame
import sys
import random
from button import Button

from model.assassin import Assassin
from model.mage import Mage
from model.melee import Melee
from model.ranger import Ranger
from model.healer import Healer
from model.barbarian import Barbarian


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
        self.available_heroes = [Assassin, Mage, Melee, Ranger, Healer, Barbarian]
        self.selected_heroes_team1 = []
        self.selected_heroes_team2 = []
        self.current_team = 1
        self.match_scores = match_scores if match_scores else [0, 0]

        # Создание кнопок для героев
        self.hero_buttons = [Button(hero.__name__, (100 + i * 150, 100), 30, "navy", hero) for i, hero in
                             enumerate(self.available_heroes)]

        # Кнопка для завершения выбора
        self.finish_button = Button("Finish", (self.window_width // 2, self.window_height - 100), 50, "green", "finish")

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(self.selected_heroes_team1) < 2 or len(self.selected_heroes_team2) < 2:
                for button in self.hero_buttons:
                    action = button.click(event)
                    if action:
                        self.pick_hero(action)
            if self.finish_button.click(event) == "finish":
                self.finish_picking()

    def pick_hero(self, hero_class):
        if self.current_team == 1 and len(self.selected_heroes_team1) < 2:
            self.selected_heroes_team1.append(hero_class)
            self.current_team = 2

            # Automatically pick a hero for team 2
            available_for_team2 = [hero for hero in self.available_heroes if
                                   hero not in self.selected_heroes_team1 and hero not in self.selected_heroes_team2]
            if available_for_team2:
                hero_class_team2 = random.choice(available_for_team2)
                self.selected_heroes_team2.append(hero_class_team2)
                # Disable the button for the picked hero
                for button in self.hero_buttons:
                    if button.feedback == hero_class_team2:
                        button.disable()
            self.current_team = 1

        # Disable the button for the picked hero
        for button in self.hero_buttons:
            if button.feedback == hero_class:
                button.disable()

    def finish_picking(self):
        if len(self.selected_heroes_team1) == 2 and len(self.selected_heroes_team2) == 2:
            from view.gameplay_view import GameplayState
            self.controller.set_state(
                GameplayState(self.controller, self.window_width, self.window_height, self.selected_heroes_team1,
                              self.selected_heroes_team2, self.game_mode, self.match_scores))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        # Отрисовка счета матча
        font = pygame.font.SysFont("Arial", 36)
        match_score_text = f"Match Score - Team 1: {self.match_scores[0]}  -  Team 2: {self.match_scores[1]}"
        match_score_surface = font.render(match_score_text, True, pygame.Color("white"))
        match_score_rect = match_score_surface.get_rect(center=(self.window_width // 2, 50))
        screen.blit(match_score_surface, match_score_rect)

        # Отрисовка кнопок героев
        for button in self.hero_buttons:
            button.check_hover()
            button.show(screen)

        # Отрисовка кнопки завершения выбора
        self.finish_button.show(screen)

        # Отрисовка выбранных героев
        small_font = pygame.font.SysFont("Arial", 24)

        team1_label = small_font.render("Team 1:", True, pygame.Color("white"))
        screen.blit(team1_label, (50, self.window_height - 250))
        for i, hero in enumerate(self.selected_heroes_team1):
            hero_text = small_font.render(hero.__name__, True, pygame.Color("white"))
            screen.blit(hero_text, (50, self.window_height - 220 + i * 30))

        team2_label = small_font.render("Team 2:", True, pygame.Color("white"))
        screen.blit(team2_label, (self.window_width - 200, self.window_height - 250))
        for i, hero in enumerate(self.selected_heroes_team2):
            hero_text = small_font.render(hero.__name__, True, pygame.Color("white"))
            screen.blit(hero_text, (self.window_width - 200, self.window_height - 220 + i * 30))

        pygame.display.flip()
