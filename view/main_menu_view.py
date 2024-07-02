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

        self.buttons = [
            Button("New Game", (window_width // 2 - 100, window_height // 2 - 100), 50, "navy", "new_game"),
            Button("Settings", (window_width // 2 - 100, window_height // 2), 50, "navy", "settings"),
            Button("Quit", (window_width // 2 - 100, window_height // 2 + 100), 50, "navy", "quit")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "new_game":
                    from view.choose_mode_view import ChooseModeState
                    self.controller.set_state(ChooseModeState(self.controller, self.window_width, self.window_height))
                elif action == "settings":
                    from view.settings_view import SettingsState
                    self.controller.set_state(SettingsState(self.controller))
                elif action == "quit":
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        for button in self.buttons:
            button.check_hover()
            button.show(screen)

        pygame.display.flip()
