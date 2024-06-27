import pygame
import sys
from button import Button

class MainMenuState:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        # Создание кнопок
        self.buttons = [
            Button("New Game", (int(self.window_width * 0.4), int(self.window_height * 0.3)), 50, "navy", "new_game"),
            Button("Settings", (int(self.window_width * 0.4), int(self.window_height * 0.5)), 50, "navy", "settings"),
            Button("Quit", (int(self.window_width * 0.4), int(self.window_height * 0.7)), 50, "navy", "quit")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "new_game":
                    from view.choose_mode_view import ChooseModeMenu  # ленивый импорт
                    self.controller.set_state(ChooseModeMenu(self.controller, self.window_width, self.window_height))
                elif action == "settings":
                    from view.settings_view import SettingsState  # ленивый импорт
                    self.controller.set_state(SettingsState(self.controller, self.window_width, self.window_height))
                elif action == "quit":
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self, screen):
        # Отрисовка фонового изображения
        screen.blit(self.background_image, (0, 0))

        # Отрисовка кнопок
        for button in self.buttons:
            button.show(screen)

        pygame.display.flip()
