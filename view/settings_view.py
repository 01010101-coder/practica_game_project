import pygame
import sys
from button import Button

class SettingsState:
    def __init__(self, controller):
        self.controller = controller
        self.buttons = [
            Button("Back", (300, 400), 50, "navy", "back")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "back":
                    from view.main_menu_view import MainMenuState  # ленивый импорт
                    self.controller.set_state(MainMenuState(self.controller))

    def update(self):
        # Пустой метод update для SettingsState
        pass

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for button in self.buttons:
            button.show(screen)
        pygame.display.flip()
