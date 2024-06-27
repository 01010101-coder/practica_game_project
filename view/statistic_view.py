from button import Button
from model.game_model import GameModel
import pygame
import sys


class StatisticMenu:
    def __init__(self, controller, window_width, window_height):
        self.controller = controller
        self.game_model = GameModel()
        self.window_width = window_width
        self.window_height = window_height

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.window_width, self.window_height))

        self.buttons = [
            Button("Next Round", (int(self.window_width * 0.4), int(self.window_height * 0.8)), 50, "navy",
                   "next_round")
        ]

        self.game_model.clear_stats()
        self.game_model.insert_stats('team_1', 'Герой_1', 5, 3, 1000, 300, 50)
        self.game_model.insert_stats('team_1', 'Герой_2', 2, 4, 800, 500, 30)
        self.game_model.insert_stats('team_1', 'Герой_3', 7, 1, 1200, 200, 60)
        self.game_model.insert_stats('team_2', 'Герой_4', 3, 5, 900, 100, 40)
        self.game_model.insert_stats('team_2', 'Герой_5', 4, 2, 1100, 400, 70)
        self.game_model.insert_stats('team_2', 'Герой_6', 6, 3, 1300, 150, 20)

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
                    self.controller.set_state(GameplayState(self.controller, self.window_width, self.window_height))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        # Отрисовка кнопок
        for button in self.buttons:
            button.show(screen)

        # Отрисовка таблицы статистики
        font = pygame.font.SysFont("Arial", 24)
        headers = ["Команда", "Убийства", "Смерти", "Урон", "Лечение", "Контроль"]
        header_x = int(self.window_width * 0.05)
        header_y = int(self.window_height * 0.1)

        # Заголовки таблицы
        for i, header in enumerate(headers):
            text_surface = font.render(header, True, pygame.Color("white"))
            screen.blit(text_surface, (header_x + i * 120, header_y))

        # Статистика команд
        stats = self.game_model.get_stats()
        for row_index, row in enumerate(stats):
            for col_index, cell in enumerate(row[1:]):  # Пропускаем id
                text_surface = font.render(str(cell), True, pygame.Color("white"))
                screen.blit(text_surface, (header_x + col_index * 120, header_y + (row_index + 1) * 30))

        pygame.display.flip()
