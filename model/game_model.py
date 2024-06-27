import sqlite3
from model.hero import Hero


class GameModel:
    def __init__(self):
        self.heroes = {
            'team_1': [Hero(200, 150), Hero(200, 400)],
            'team_2': [Hero(500, 150), Hero(500, 400)]
        }
        self.scores = [0, 0]

        self.connection = None
        self.cursor = None

        self.create_db()

    def update(self):
        for hero in self.heroes['team_1']:
            hero.logic(self.heroes['team_1'], self.heroes['team_2'])
        for hero in self.heroes['team_2']:
            hero.logic(self.heroes['team_2'], self.heroes['team_1'])

    def create_db(self):
        self.connection = sqlite3.connect("game_stats.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS statistics (
                                id INTEGER PRIMARY KEY,
                                team TEXT,
                                hero_name TEXT,
                                kills INTEGER,
                                deaths INTEGER,
                                damage INTEGER,
                                healing INTEGER,
                                control INTEGER)''')

        self.connection.commit()

    def insert_stats(self, team, hero_name, kills, deaths, damage, healing, control):
        self.cursor.execute('''INSERT INTO statistics (team, hero_name, kills, deaths, damage, healing, control)
                               VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (team, hero_name, kills, deaths, damage, healing, control))
        self.connection.commit()

    def get_stats(self):
        self.cursor.execute('''SELECT * FROM statistics''')
        return self.cursor.fetchall()

    def clear_stats(self):
        self.cursor.execute('''DELETE FROM statistics''')
        self.connection.commit()
