import pygame
import sys
from button import Button

class SettingsState:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.window_width = window_width
        self.window_height = window_height
        self.buttons = [
            Button("Back", (int(self.window_width * 0.4), int(self.window_height * 0.7)), 50, "navy", "back")
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
                    self.controller.set_state(MainMenuState(self.controller, self.window_width, self.window_height))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for button in self.buttons:
            button.show(screen)
        pygame.display.flip()
