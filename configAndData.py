import os
import json


#miscconf
windows_username = os.getlogin()
repertoire_logs = os.path.join("C:\\", "Users", windows_username, "Saved Games", "Frontier Developments", "Elite Dangerous")
font_path = os.path.abspath("C:\\Edsharefsdtarget\\Edsharefsdtarget\\elitedanger.ttf")  # Remplacez le chemin par le chemin complet vers votre fichier de police


json_file_path = "config_and_data.json"

#  si  fichier JSON existe déjà
if os.path.exists(json_file_path):
    with open(json_file_path, "r") as existing_json_file:
        config_data = json.load(existing_json_file)
else:
    # Si le fichier n'existe pas, utliser le modèle de données par défaut
    template_data = {
        "my_commander": {
            "name": "",
            "api_key": "",
            "current_StarSystem": "",
            "FSDTarget": ""
        },
        "wingman1": {
            "name": "",
            "api_key": "",
            "current_StarSystem": "",
            "FSDTarget": ""
        }
    }
    with open(json_file_path, "w") as new_json_file:
        json.dump(template_data, new_json_file, indent=4)


# parcour du JSON pour trouver la key en fonction du cmdrnom 
def get_wingmankeydependingName(commander_name):
    with open("config_and_data.json", "r") as json_file:
        data = json.load(json_file)
    found_key = None
    for key, value in data.items():
        if isinstance(value, dict) and "name" in value and value["name"] == commander_name:
            found_key = key
            break
    return key