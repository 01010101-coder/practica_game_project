# view/game_view.py
import pygame

class GameView:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill((255, 255, 255))
        heroes = self.model.heroes

        for hero in heroes:
            pygame.draw.circle(self.screen, (255, 0, 0), hero.position, 20)

        pygame.display.flip()