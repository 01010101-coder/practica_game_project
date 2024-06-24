class GameModel: # модель для управления игрой
    def __init__(self):
        self.heroes = { # герои команд
            'team_1': [],
            'team_2': []
        }

        self.spells_stack = [] # заклинания хода


    def add_hero(self, hero): # добавить героя в игру
        self.heroes.append(hero)

    def update(self):
        # Логика обновления состояния игры
        pass

