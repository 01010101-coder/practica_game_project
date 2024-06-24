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
    Hero3 = Hero(30, 70)

    model.add_hero(Hero1, 1)
    model.add_hero(Hero3, 1)
    model.add_hero(Hero2, 2)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Hero1.logic(model.heroes['team_1'], model.heroes['team_2'])
        Hero2.logic(model.heroes['team_2'], model.heroes['team_1'])

        view.draw()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
