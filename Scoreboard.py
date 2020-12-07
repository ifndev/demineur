from typing import List, Dict, Union
import datetime as dt
import csv


def compare_entries(entry1: Dict[str, Union[str, int]], entry2: Dict[str, Union[str, int]]) -> bool:
    return entry1['score'] <= entry2['score']


def stringify_winner(winner):
    return f"{winner['name']} - {winner['score']} pts (le {winner['date']})"


class Scoreboard:
    def __init__(self):
        try:
            # Récupérons le scoreboard s'il existe
            file = open("scoreboard.csv", "r")
            self.__scoreboard = list(csv.DictReader(file, delimiter=','))
        except IOError:
            # Si vide, on initialise avec un premier gagnant!
            self.__scoreboard = [{'name': 'ifnvitch', 'score': '42', 'date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]

    def get_scoreboard(self) -> List[Dict[str, Union[str, int]]]:
        return self.__scoreboard

    def add_to_scoreboard(self, name: str, score: int):
        self.__scoreboard.append({'name': name, 'score': score, 'date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        self.__scoreboard.sort(key=compare_entries)

    def save_scoreboard(self):
        with open("scoreboard.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'score', 'date'])
            writer.writeheader()
            writer.writerows(self.__scoreboard)
