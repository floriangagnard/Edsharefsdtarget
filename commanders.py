import json
from typing import List
from commander import Commander

# Commander Class et methodes utilitaires 
class Commanders:

    @staticmethod
    def build(myjson) -> Commander: 
        return Commander(myjson['name'],myjson['key'],myjson['position'],myjson['target'])

    @staticmethod
    def serialize(commanders : List[Commander]):
        """
        Methode permettantde serialiser une liste de commander
        """
        return  json.dumps(commanders, indent=4, default=lambda o: o.__dict__)

    @staticmethod
    def deserialize(json_string : str ):
        """
        Methode statique permettant de creer une instance de commander à partir d'une string JSON
        """
        myListjson = json.loads(json_string, object_hook=Commanders.build)
        return myListjson
       



