from model.hero import Hero

class GameModel:
    def __init__(self):
        self.heroes = {
            'team_1': [Hero(100, 100), Hero(150, 100)],
            'team_2': [Hero(100, 300), Hero(150, 300)]
        }

        self.mode = None

        self.round = 0

    def update(self):
        for hero in self.heroes['team_1']:
            hero.logic(self.heroes['team_1'], self.heroes['team_2'])
        for hero in self.heroes['team_2']:
            hero.logic(self.heroes['team_2'], self.heroes['team_1'])