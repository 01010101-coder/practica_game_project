import pygame
from controller.game_controller import GameController
from view.main_menu_view import MainMenuState

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Example with MVC and State Management")

    controller = GameController()
    controller.set_state(MainMenuState(controller))

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            controller.handle_event(event)

        controller.update()
        controller.draw(screen)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
