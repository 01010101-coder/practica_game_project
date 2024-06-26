import pygame
import sys
from button import Button

class MainMenuState:
    def __init__(self, controller):
        self.controller = controller
        self.buttons = [
            Button("New Game", (300, 200), 50, "navy", "new_game"),
            Button("Settings", (300, 300), 50, "navy", "settings"),
            Button("Quit", (300, 400), 50, "navy", "quit")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "new_game":
                    from view.choose_mode_view import ChooseModeMenu
                    self.controller.set_state(ChooseModeMenu(self.controller))
                elif action == "settings":
                    from view.settings_view import SettingsState  # ленивый импорт
                    self.controller.set_state(SettingsState(self.controller))
                elif action == "quit":
                    pygame.quit()
                    sys.exit()

    def update(self):
        # Пустой метод update для MainMenuState
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for button in self.buttons:
            button.show(screen)
        pygame.display.flip()
