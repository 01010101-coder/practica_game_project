import pygame
import sys
from button import Button


class SettingsState:
    def __init__(self, controller):
        self.controller = controller
        self.volume = pygame.mixer.music.get_volume()
        self.music_enabled = pygame.mixer.music.get_busy()

        # Загрузка фонового изображения
        self.background_image = pygame.image.load("view/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1300, 700))

        self.buttons = [
            Button("Volume Up", (300, 200), 50, feedback="volume_up"),
            Button("Volume Down", (300, 300), 50, feedback="volume_down"),
            Button("Stop Music", (300, 400), 50, feedback="toggle_music"),
            Button("Back", (300, 500), 50, feedback="back")
        ]
        self.selected_button = 0
        self.buttons[self.selected_button].hover = True

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.buttons[self.selected_button].hover = False
                self.selected_button = (self.selected_button + 1) % len(self.buttons)
                self.buttons[self.selected_button].hover = True
            elif event.key == pygame.K_UP:
                self.buttons[self.selected_button].hover = False
                self.selected_button = (self.selected_button - 1) % len(self.buttons)
                self.buttons[self.selected_button].hover = True
            elif event.key == pygame.K_RETURN:
                self.activate_button()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                action = button.click(event)
                if action:
                    self.activate_button_by_feedback(action)

    def activate_button(self):
        action = self.buttons[self.selected_button].feedback
        self.activate_button_by_feedback(action)

    def activate_button_by_feedback(self, feedback):
        if feedback == "volume_up":
            self.volume = min(self.volume + 0.1, 1.0)
            pygame.mixer.music.set_volume(self.volume)
        elif feedback == "volume_down":
            self.volume = max(self.volume - 0.1, 0.0)
            pygame.mixer.music.set_volume(self.volume)
        elif feedback == "toggle_music":
            if self.music_enabled:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1)
            self.music_enabled = not self.music_enabled
        elif feedback == "back":
            from view.main_menu_view import MainMenuState
            self.controller.set_state(MainMenuState(self.controller, 1300, 700))

    def update(self):
        for button in self.buttons:
            button.check_hover()

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))  # Отображение фонового изображения
        for button in self.buttons:
            button.show(screen)
        pygame.display.flip()
