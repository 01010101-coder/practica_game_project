class GameModel:
    def __init__(self, team_1, team_2, game_mode):
        self.heroes = {
            'team_1': [hero_class(300, 330 + i * 100, 0) for i, hero_class in enumerate(team_1)],
            'team_2': [hero_class(1100, 330 + i * 100, 1) for i, hero_class in enumerate(team_2)]
        }

        self.game_mode = game_mode
        self.scores = [0, 0]
        self.kills = {
            'team_1': 0,
            'team_2': 0
        }
        self.match_scores = [0, 0]  # Счет матчей (побед)
        self.total_matches = 3 if game_mode == "bo3" else 5

    def update(self):
        for hero in self.heroes['team_1']:
            hero.logic(self, self.heroes['team_1'], self.heroes['team_2'])
        for hero in self.heroes['team_2']:
            hero.logic(self, self.heroes['team_2'], self.heroes['team_1'])

        if self.scores[0] >= 15 or self.scores[1] >= 15:
            if self.scores[0] >= 15:
                self.match_scores[0] += 1
            else:
                self.match_scores[1] += 1
            self.reset_scores()
            return True
        return False 

    def reset_scores(self):
        self.scores = [0, 0]
        for hero in self.heroes['team_1']:
            hero.hp = hero.max_hp
            hero.position = hero.startpos.copy()
        for hero in self.heroes['team_2']:
            hero.hp = hero.max_hp
            hero.position = hero.startpos.copy()

    def is_series_over(self):
        if self.match_scores[0] > self.total_matches // 2 or self.match_scores[1] > self.total_matches // 2:
            return True
        return False
