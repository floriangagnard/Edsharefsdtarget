
from typing import List
import json
from commander import Commander
class Crew:
    def __init__(self, mainCommander: Commander, wingmen : List[Commander]):
        self.commander = mainCommander
        self.wingmen = wingmen
    def serialize(self):
        """
        Methode permettantde serialiser l'instance du crew en json
        """
        return  json.dumps(self, indent=4, default=lambda o: o.__dict__)