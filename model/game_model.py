from model.melee import Melee
from model.ranger import Ranger
from model.mage import Mage
from model.assassin import Assassin

class GameModel:
    def __init__(self):
        self.heroes = {
            'team_1': [Melee(200, 150), Melee(200, 400)],  # Корректировка координат героев
            'team_2': [Assassin(500, 150), Assassin(500, 400)]
        }

        self.scores = [0, 0]

    def update(self):
        print(self.scores)
        for hero in self.heroes['team_1']:
            hero.logic(self.heroes['team_1'], self.heroes['team_2'], self.scores[1])
        for hero in self.heroes['team_2']:
            hero.logic(self.heroes['team_2'], self.heroes['team_1'], self.scores[0])

