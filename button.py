import pygame

class Button:
    def __init__(self, text, pos, font, bg=None, feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg, feedback)
        self.hover = False
        self.enabled = True

    def change_text(self, text, bg=None, feedback=""):
        self.text = text
        self.bg = bg
        self.feedback = feedback
        self.render_text()

    def render_text(self):
        self.text_render = self.font.render(self.text, True, pygame.Color("white"))
        self.size = self.text_render.get_size()
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)  # Использование прозрачного фона
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        if self.bg:
            self.surface.fill(self.bg)
        self.surface.blit(self.text_render, (0, 0))

    def show(self, screen):
        if not self.enabled:
            self.surface.fill((128, 128, 128, 128))  # Серый фон с прозрачностью
        elif self.hover:
            self.surface.fill((30, 144, 255, 128))  # DodgerBlue фон с прозрачностью
        else:
            self.surface.fill((0, 0, 0, 0))  # Прозрачный фон
        self.surface.blit(self.text_render, (0, 0))
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        if not self.enabled:
            return None
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.feedback

    def check_hover(self):
        if not self.enabled:
            self.hover = False
            return
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.hover = True
        else:
            self.hover = False

    def disable(self):
        self.enabled = False
        self.change_text(self.text, "gray", self.feedback)