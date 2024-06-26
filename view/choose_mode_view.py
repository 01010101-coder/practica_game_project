import pygame
import sys
from model.game_model import GameModel
from button import Button

class ChooseModeMenu:
    def __init__(self, controller):
        self.controller = controller
        self.model = GameModel()
        self.buttons = [
            Button("Bo3", (300, 200), 50, "navy", "mode_bo3"),
            Button("Bo5", (300, 300), 50, "navy", "mode_bo5"),
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
                    from view.gameplay_view import GameplayState
                    self.model.mode = "bo3"
                    self.controller.set_state(GameplayState(self.controller))
                elif action == "mode_bo5":
                    from view.gameplay_view import GameplayState
                    self.model.mode = "bo5"
                    self.controller.set_state(GameplayState(self.controller))
                elif action == "back":
                    from view.main_menu_view import MainMenuState
                    self.controller.set_state(MainMenuState(self.controller))


    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for button in self.buttons:
            button.show(screen)
        pygame.display.flip()
