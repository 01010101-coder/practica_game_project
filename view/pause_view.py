import pygame
import sys
from button import Button

class PauseState:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        # Создание кнопок
        self.resume_button = Button("Resume", (self.window_width // 2 - 50, self.window_height // 2 - 100), 30, "green", "resume")
        self.main_menu_button = Button("Main Menu", (self.window_width // 2 - 50, self.window_height // 2), 30, "red", "main_menu")

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button.click(event) == "resume":
                self.controller.set_state(self.controller.previous_state)
            elif self.main_menu_button.click(event) == "main_menu":
                from view.main_menu_view import MainMenuState
                self.controller.set_state(MainMenuState(self.controller, 1300, 700))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.controller.set_state(self.controller.previous_state)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        # Отрисовка кнопок
        self.resume_button.show(screen)
        self.main_menu_button.show(screen)

        pygame.display.flip()
