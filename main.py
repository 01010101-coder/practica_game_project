# main.py
import pygame
from model.game_model import GameModel
from model.heroes.hero import Hero
from view.game_view import GameView
from controller.game_controller import GameController

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    model = GameModel()
    view = GameView(model, screen)
    controller = GameController(model)

    Hero1 = Hero(30, 30)
    Hero2 = Hero(350, 300)

    model.add_hero(Hero1)
    model.add_hero(Hero2)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        view.draw()
        Hero1.logic()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
