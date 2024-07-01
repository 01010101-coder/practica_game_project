import pygame
import sys
from controller.game_controller import GameController
from view.main_menu_view import MainMenuState

def main():
    pygame.init()
    pygame.mixer.init()  # Инициализация микшера Pygame

    window_weight = 1300
    window_height = 700

    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)  # -1 означает бесконечное повторение
    pygame.mixer.music.set_volume(0.5)  # Установка громкости на 50%

    screen = pygame.display.set_mode((window_weight, window_height))
    pygame.display.set_caption("Game Example with MVC and State Management")

    controller = GameController()
    controller.set_state(MainMenuState(controller, window_weight, window_height))

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
