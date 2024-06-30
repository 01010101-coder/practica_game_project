import pygame
import sys
from button import Button

class GameOverState:
    def __init__(self, controller, match_scores, window_width, window_height):
        self.controller = controller
        self.match_scores = match_scores
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        # Создание кнопки для выхода в главное меню
        self.main_menu_button = Button("Main Menu", (self.window_width // 2 - 100, self.window_height // 2 + 100), 50, "green", "main_menu")

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.main_menu_button.click(event) == "main_menu":
                from view.main_menu_view import MainMenuState
                self.controller.set_state(MainMenuState(self.controller, 1300, 600))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        screen.fill((0, 0, 0, 150), special_flags=pygame.BLEND_RGBA_MULT)  # Затемнение фона

        font = pygame.font.SysFont("Arial", 48)
        if self.match_scores[0] > self.match_scores[1]:
            text = "Team 1 Wins the Series!"
        else:
            text = "Team 2 Wins the Series!"
        text_surface = font.render(text, True, pygame.Color("white"))
        text_rect = text_surface.get_rect(center=(self.window_width // 2, self.window_height // 2))
        screen.blit(text_surface, text_rect)

        # Отрисовка кнопки для выхода в главное меню
        self.main_menu_button.show(screen)

        pygame.display.flip()
