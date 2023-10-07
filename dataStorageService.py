
import os
from commander import Commander

mainCommanderFile = "mainCommanderData.json"
wingManCommandersFile = "wingManCommandersFile.json"

def read_main_commander():
    if os.path.exists(mainCommanderFile):
        with open(mainCommanderFile, "r") as existing_json_file:
            return Commander.commander_deserialize(existing_json_file.read())
    else:
        return Commander("default Commander","invalid","nowhere","nowhere")


def write_main_commander(commander: Commander):
    """
    sauvegarde les données du main commander
    """
    data = commander.commander_serialize()
    f = open(mainCommanderFile, "w")
    f.write(data)
    f.close()