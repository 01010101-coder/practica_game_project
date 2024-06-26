class GameController:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state
        self.state.controller = self

    def handle_event(self, event):
        if self.state:
            self.state.handle_event(event)

    def update(self):
        if self.state:
            self.state.update()

    def draw(self, screen):
        if self.state:
            self.state.draw(screen)
