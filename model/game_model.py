class GameModel: # модель для управления игрой
    def __init__(self):
        self.heroes = {  # герои команд
            'team_1': [],
            'team_2': []
        }

        self.spells_stack = [] # заклинания хода


    def add_hero(self, hero, team): # добавить героя в игру
        if team == 1:
            self.heroes['team_1'].append(hero)
        if team == 2:
            self.heroes['team_2'].append(hero)

    def update(self):
        # Логика обновления состояния игры
        pass

