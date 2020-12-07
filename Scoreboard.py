from typing import List, Dict, Union
import datetime


def compare_entries(entry1: Dict[str, Union[str, int]], entry2: Dict[str, Union[str, int]]) -> bool:
    return entry1['score'] <= entry2['score']


def stringify_winner(winner):
    return f"{winner['name']} - {winner['score']} pts (le {winner['date'].strftime('%Y-%m-%d %H:%M:%S')})"


class Scoreboard:
    def __init__(self):
        self.__scoreboard = [{'name': 'ifnvitch', 'score': 42, 'date': datetime.datetime.now()}]

    def get_scoreboard(self) -> List[Dict[str, Union[str, int]]]:
        return self.__scoreboard

    def add_to_scoreboard(self, name: str, score: int):
        self.__scoreboard.append({'name': name, 'score': score, 'date': datetime.datetime.now()})
        self.__scoreboard.sort(key=compare_entries)
