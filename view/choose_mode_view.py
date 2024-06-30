import pygame
import sys
from button import Button
from view.pick_menu import PickMenuState
from view.main_menu_view import MainMenuState

class ChooseModeMenu:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        # Создание кнопок для выбора режима игры
        self.buttons = [
            Button("Best of 3", (300, 200), 50, "navy", "mode_bo3"),
            Button("Best of 5", (300, 300), 50, "navy", "mode_bo5"),
            Button("Back", (300, 400), 50, "navy", "back")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "mode_bo3":
                    self.controller.set_state(PickMenuState(self.controller, self.window_width, self.window_height, "bo3"))
                elif action == "mode_bo5":
                    self.controller.set_state(PickMenuState(self.controller, self.window_width, self.window_height, "bo5"))
                elif action == "back":
                    self.controller.set_state(MainMenuState(self.controller, 1300, 600))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for button in self.buttons:
            button.show(screen)
        pygame.display.flip()
