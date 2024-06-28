from model.melee import Melee
from model.ranger import Ranger
from model.mage import Mage
from model.assassin import Assassin

class GameModel:
    def __init__(self, team_1, team_2, game_mode):
        self.heroes = {
            'team_1': team_1,  # Корректировка координат героев
            'team_2': team_2
        }

        self.game_mode = game_mode

        self.scores = [0, 0]

    def update(self):
        print(self.scores)
        for hero in self.heroes['team_1']:
            hero.logic(self.heroes['team_1'], self.heroes['team_2'], self.scores[1])
        for hero in self.heroes['team_2']:
            hero.logic(self.heroes['team_2'], self.heroes['team_1'], self.scores[0])

