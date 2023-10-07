
import os
from typing import List
from commander import Commander
from commanders import Commanders

mainCommanderFile = "mainCommanderData.json"
wingManCommandersFile = "wingmenData.json"

def read_main_commander() -> Commander:
    if os.path.exists(mainCommanderFile):
        with open(mainCommanderFile, "r") as existing_json_file:
            return Commander.deserialize(existing_json_file.read())
    else:
        return Commander("default Commander","invalid","nowhere","nowhere")


def write_main_commander(commander: Commander):
    """
    sauvegarde les données du main commander
    """
    data = commander.serialize()
    f = open(mainCommanderFile, "w")
    f.write(data)
    f.close()

def read_wingmens_commanders() ->  List[Commander] :


    if os.path.exists(mainCommanderFile):
        with open(wingManCommandersFile, "r") as existing_json_file:
            return Commanders.deserialize(existing_json_file.read())
    else:
        return Commander("default Commander","invalid","nowhere","nowhere")


def write_wingmens_commanders(commanders:  List[Commander]):
    """
    sauvegarde les données des ailiés commander
    """
    data =  Commanders.serialize(commanders)
    f = open(wingManCommandersFile, "w")
    f.write(data)
    f.close()

