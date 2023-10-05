import json
import os
import glob
import time
import configAndData
import json

#TEMP 
import api_interaction
######





FSDTarget = ""
current_StarSystem = ""

def get_FSDTargetAndStarSystem(last_log):
    global current_StarSystem, FSDTarget, Your_name

    try:
        with open(last_log, 'r') as fichier:
            for ligne in fichier:
                evenement = json.loads(ligne.strip())
                if evenement.get("event") == "FSDTarget":
                    FSDTarget = evenement.get("Name")
                if evenement.get("event") == "Location":
                    current_StarSystem = evenement.get("StarSystem")
        
            print(f"FSDTarget :" + FSDTarget)
            print(f"Position actuelle : " + current_StarSystem)
            with open("config_and_data.json", "r+") as json_file:
                data = json.load(json_file)
                data["my_commander"]["FSDTarget"] = FSDTarget
                data["my_commander"]["current_StarSystem"] = current_StarSystem
                json_file.seek(0)
                json.dump(data, json_file, indent=4)
                json_file.truncate()


            #a modifier si j'en fais une option
            if 1==1:
                api_interaction.send_comment_to_api(data["my_commander"]["name"], data["my_commander"]["api_key"], current_StarSystem, FSDTarget)

        #return FSDTarget, current_StarSystem

    except Exception as e:
        print(f"Erreur: {str(e)}")
        return None

# Verif de la taille du log pour voir si un event se produit
def checkLogUpdate(last_log):
    taille_actuelle = 0

    while True:
        try:
            taille = os.path.getsize(last_log)

            if taille != taille_actuelle:
                get_FSDTargetAndStarSystem(last_log)
                taille_actuelle = taille
            time.sleep(1)
        except Exception as e:
            print(f"Erreur: {str(e)}")

def get_lastLogToParse(repertoire_logs):
    fichiers_logs = glob.glob(os.path.join(repertoire_logs, '*.log'))

    # tri des fichiers par date de création (récent en 1er)
    fichiers_logs_tries = sorted(fichiers_logs, key=lambda x: os.path.getctime(x), reverse=True)

    if fichiers_logs_tries:
        return fichiers_logs_tries[0]
    else:
        return None

def run_log_monitor():

    while True:
        last_log = get_lastLogToParse(configAndData.repertoire_logs)
        if last_log:
            checkLogUpdate(last_log)

        time.sleep(300)  #5 minutes => check for a new log

if __name__ == "__main__":
    run_log_monitor()