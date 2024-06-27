import pygame
import sys
from model.game_model import GameModel
from button import Button

class ChooseModeMenu:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.model = GameModel()
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        # Создание кнопок
        self.buttons = [
            Button("Bo3", (int(self.window_width * 0.4), int(self.window_height * 0.3)), 50, "navy", "mode_bo3"),
            Button("Bo5", (int(self.window_width * 0.4), int(self.window_height * 0.5)), 50, "navy", "mode_bo5"),
            Button("Back", (int(self.window_width * 0.4), int(self.window_height * 0.7)), 50, "navy", "back")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "mode_bo3":
                    from view.gameplay_view import GameplayState  # ленивый импорт
                    self.model.mode = "bo3"
                    self.controller.set_state(GameplayState(self.controller, self.window_width, self.window_height))
                elif action == "mode_bo5":
                    from view.gameplay_view import GameplayState  # ленивый импорт
                    self.model.mode = "bo5"
                    self.controller.set_state(GameplayState(self.controller, self.window_width, self.window_height))
                elif action == "back":
                    from view.main_menu_view import MainMenuState  # ленивый импорт
                    self.controller.set_state(MainMenuState(self.controller, self.window_width, self.window_height))

    def update(self):
        pass

    def draw(self, screen):
        # Отрисовка фонового изображения
        screen.blit(self.background_image, (0, 0))

        # Отрисовка кнопок
        for button in self.buttons:
            button.show(screen)

        pygame.display.flip()
