import pygame
from controller.game_controller import GameController
from view.main_menu_view import MainMenuState
from view.gameplay_view import GameplayState

def main():
    pygame.init()
    pygame.font.init()  # Инициализация модуля шрифтов Pygame

    # Настройки размеров окна
    window_width = 1300
    window_height = 600

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Game Example with MVC and State Management")

    controller = GameController()
    # controller.set_state(MainMenuState(controller, window_width, window_height))
    controller.set_state(GameplayState(controller, window_width, window_height))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            controller.handle_event(event)

        controller.update()
        controller.draw(screen)

        # Проверка наведения для всех кнопок в текущем состоянии
        if hasattr(controller.state, 'buttons'):
            for button in controller.state.buttons:
                button.check_hover()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
