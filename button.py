import pygame

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg, feedback)
        self.hover = False

    def change_text(self, text, bg="black", feedback=""):
        self.text = text
        self.bg = bg
        self.feedback = feedback
        self.render_text()

    def render_text(self):
        self.text_render = self.font.render(self.text, True, pygame.Color("white"))
        self.size = self.text_render.get_size()
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.surface.fill(self.bg)
        self.surface.blit(self.text_render, (0, 0))

    def show(self, screen):
        if self.hover:
            self.surface.fill(pygame.Color("dodgerblue"))
        else:
            self.surface.fill(self.bg)
        self.surface.blit(self.text_render, (0, 0))
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.feedback

    def check_hover(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.hover = True
        else:
            self.hover = False
