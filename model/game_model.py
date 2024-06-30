class GameModel:
    def __init__(self, team_1, team_2, game_mode):
        self.heroes = {
            'team_1': [hero_class(400, 300 + i * 100, 1) for i, hero_class in enumerate(team_1)],
            'team_2': [hero_class(900, 300 + i * 100, 2) for i, hero_class in enumerate(team_2)]
        }
        print(self.heroes)

        self.game_mode = game_mode
        self.scores = [0, 0]

    def update(self):
        for hero in self.heroes['team_1']:
            hero.logic(self, self.heroes['team_1'], self.heroes['team_2'])
        for hero in self.heroes['team_2']:
            hero.logic(self, self.heroes['team_2'], self.heroes['team_1'])
