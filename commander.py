import json

# Commander Class et methodes utilitaires 
class Commander:
    def __init__(self, name : str, key : str, position : str, target : str) -> None :
        self.name = name
        self.key = key
        self.position = position
        self.target = target


    def update_target(self,target) -> None:
        self.target = target

    def update_position(self,position) -> None:
        self.position = position



    def serialize(self) -> str:
        """
        Methode permettantde serialiser l'instance du commander en json
        """
        return  json.dumps(self, indent=4, default=lambda o: o.__dict__)

    def to_string(self):
        """
        Methode permettant de serialiser l'instance du commander en json
        """
        return  self.name + " at " + self.position

    @staticmethod
    def deserialize(json_string : str ) :
        """
        Methode statique permettant de creer une instance de commander à partir d'une string JSON
        """
        myjson = json.loads(json_string)
        return Commander(myjson['name'],myjson['key'],myjson['position'],myjson['target'])


