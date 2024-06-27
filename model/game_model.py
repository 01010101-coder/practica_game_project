from model.hero import Hero

class GameModel:
    def __init__(self):
        self.heroes = {
            'team_1': [Hero(200, 150), Hero(200, 400)],  # Корректировка координат героев
            'team_2': [Hero(500, 150), Hero(500, 400)]
        }

        self.scores = [0, 0]

    def update(self):
        for hero in self.heroes['team_1']:
            hero.logic(self.heroes['team_1'], self.heroes['team_2'])
        for hero in self.heroes['team_2']:
            hero.logic(self.heroes['team_2'], self.heroes['team_1'])

