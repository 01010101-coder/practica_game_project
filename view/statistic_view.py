from button import Button
from model.game_model import GameModel
import pygame
import sys

class StatisticMenu:
    def __init__(self, controller):
        self.controller = controller
        self.game_model = GameModel()
        self.buttons = [
            Button("Next Round", (100, 500), 50, "navy", "next_round")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action == "next_round":
                    from view.gameplay_view import GameplayState
                    self.game_model.round += 1
                    self.controller.set_state(GameplayState(self.controller))

    def update(self):
        pass

    def draw(self, screen):
        pass
