
import os
from typing import List
from commander import Commander
from commanders import Commanders
from context import Context
from log import LogEntry
import pyperclip

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

##########################

def read_last_linelogfile(context: Context,event,path):
    if "Journal." not in path:
        return ""
    #context.add_to_logs(f"read_last_linelogfile {event} : {path}")
    if os.path.exists(path):
        with open(path, "r") as file:
            arrayLogs = []
            lines =  file.readlines()
            lastline = lines[-1]
            lastlogEntry = LogEntry.deserialize(lastline)
            arrayLogs = [lastlogEntry]
            for x in range(2,5):
                currentlineread = lines[-x] 
                currentlog = LogEntry.deserialize(currentlineread)
                if lastlogEntry.timestamp == currentlog.timestamp :
                    arrayLogs.append(currentlog)

            context.add_to_logs(f"Traitement de {len(arrayLogs)} at {lastlogEntry.timestamp}")
            for logEntry in arrayLogs:
                context.add_to_logs(f" DEBUG **{logEntry.event}**")

            for logEntry in arrayLogs:
                context.add_to_logs(f" Run on **{logEntry.event}**")
                if logEntry.event=="FSDTarget" :
                    context.add_to_logs(f"Declenchement : {logEntry.event} : __{logEntry.timestamp}__")
                    # TODO detection de changement
                    context.crew.commander.target = logEntry.name
                    pyperclip.copy(context.crew.commander.target)
                    context.action_publish_target()
                    context.action_publish_targetV2()
                if logEntry.event == "SupercruiseExit":
                    context.add_to_logs(f"Declenchement: {logEntry.event} : __{logEntry.timestamp}__")
                    context.crew.commander.position = logEntry.star_system
                if logEntry.event == "SupercruiseEntry":
                    context.add_to_logs(f"Declenchement: {logEntry.event} : __{logEntry.timestamp}__")
                    context.crew.commander.position = logEntry.star_system                
    else:
        return ""
    

