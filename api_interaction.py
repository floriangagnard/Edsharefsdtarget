import requests
import schedule
import pyperclip
import time
import json
from configAndData import get_wingmankeydependingName

# Envoyer son FSDtarget à EDSM
def send_comment_to_api(commander_name, api_key, system_name, comment):
    try:
        params = {
            "commanderName": commander_name,
            "apiKey": api_key,
            "systemName": system_name,
            "comment": comment
        }

        url = "https://www.edsm.net/api-logs-v1/set-comment"
        response = requests.get(url, params=params)

        # response JSON
        if response.status_code == 200:
            data = response.json()
            if data['msgnum'] == 100:
                print("Commentaire ajouté avec succès.")
            else:
                print(f"Erreur lors de l'ajout du commentaire : {data['msg']}")
        else:
            print(f"Erreur lors de la requête à l'API EDSM. Code de statut : {response.status_code}")

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# get le systeme actuel d'un wingman ppar EDSM
def get_wingman_current_StarSystem(wingman_commander_name, wingman_api_key):
    #try:
        params = {
            "commanderName": wingman_commander_name,
            "apiKey": wingman_api_key,
        }

        url = "https://www.edsm.net/api-logs-v1/get-position"
        response = requests.get(url, params=params)

        if response.status_code == 200:
                    apiResponse = response.json()
                    if apiResponse['msgnum'] == 100:
                        wingman_current_StarSystem = apiResponse['system']
                        print(wingman_commander_name+" est sur "+wingman_current_StarSystem)

                        with open("config_and_data.json", "r+") as json_file:
                            data = json.load(json_file)
                            key = get_wingmankeydependingName(wingman_commander_name)
                            data[key]["current_StarSystem"] = wingman_current_StarSystem
                            json_file.seek(0)
                            json.dump(data, json_file, indent=4)
                            json_file.truncate()

                    else:
                        print(f"Erreur lors de la récupération du commentaire : {apiResponse['msg']}")
        else:
            print(f"Erreur lors de la requête à l'API EDSM. Code de statut : {response.status_code}")

    #except Exception as e:
    #    print(f"Une erreur s'est produite : {str(e)}")


# get le FSDtarget du wingman 1 par l'API EDSM qui est un commentaire
def get_wingman_comment(wingman_commander_name, wingman_api_key):
    try:
        # recup de la position actuelle depuis le json

        with open("config_and_data.json", "r") as json_file:
                data = json.load(json_file)
                key = get_wingmankeydependingName(wingman_commander_name)
                wingman_current_StarSystem = data[key]["current_StarSystem"]


       
        params = {
            "commanderName": wingman_commander_name,
            "apiKey": wingman_api_key,
            "systemName": wingman_current_StarSystem
        }

        
        url = "https://www.edsm.net/api-logs-v1/get-comment"
        response = requests.get(url, params=params)

        # response JSON
        if response.status_code == 200:
            apiResponse = response.json()
            if apiResponse['msgnum'] == 100:
                comment = apiResponse['comment']
                print(f"Commentaire récupéré : {comment}")

                with open("config_and_data.json", "r+") as json_file:
                    data = json.load(json_file)
                    key = get_wingmankeydependingName(wingman_commander_name)
                    data[key]["FSDTarget"] = comment
                    json_file.seek(0)
                    json.dump(data, json_file, indent=4)
                    json_file.truncate()
                    return comment
            
            elif apiResponse['msgnum'] == 101:
                comment = apiResponse['comment']
                print("pas de FSD TARGET trouvé pour ce système ")

                with open("config_and_data.json", "r+") as json_file:
                    data = json.load(json_file)
                    key = get_wingmankeydependingName(wingman_commander_name)
                    data[key]["FSDTarget"] = ""
                    json_file.seek(0)
                    json.dump(data, json_file, indent=4)
                    json_file.truncate()
                    return ""                
            else:
                print(f"Erreur lors de la récupération du commentaire : {data['msg']}")
        else:
            print(f"Erreur lors de la requête à l'API EDSM. Code de statut : {response.status_code}")

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")


