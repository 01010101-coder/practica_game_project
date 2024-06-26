import pygame
from model.game_model import GameModel
import sys

class GameplayState:
    def __init__(self, controller):
        self.controller = controller
        self.model = GameModel()
        self.view = GameView(self.model)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def update(self):
        self.model.update()

    def draw(self, screen):
        self.view.draw(screen)

class GameView:
    def __init__(self, model):
        self.model = model

    def draw(self, screen):
        screen.fill((255, 255, 255))
        heroes = self.model.heroes['team_1'] + self.model.heroes['team_2']

        for hero in heroes:
            pygame.draw.circle(screen, (255, 0, 0), hero.position, 20)

        pygame.display.flip()
