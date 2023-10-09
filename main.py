
import time
starttime = time.time()

import threading
from crew import Crew
from context import Context
from consoleview import ConsoleView
from watchdog.observers import Observer
from logwatch import LogEDFile, path
from serveurPlug import create_application
import dataStorageService
import pyttsx3


## Initilisation du Commander
mainCommander = dataStorageService.read_main_commander()
listWingMan = dataStorageService.read_wingmens_commanders()
crew = Crew(mainCommander,listWingMan)


context = Context(crew= crew)

app = ConsoleView(context)

observer = Observer()
observer.schedule(LogEDFile(context=context,  callback=dataStorageService.read_last_linelogfile), path)
observer.start()


apith = threading.Thread(target=create_application, args=("nnn",context ) )
apith.daemon = True  # Le thread se terminera lorsque l'application principale se terminera
apith.start()


engine = pyttsx3.init()
voice_enabled = False
text_to_speak = "Bienvenue Commandeur"
engine.say(text_to_speak)
engine.runAndWait()

while True:
    app.render()
    # Remove the Time taken by code to execute
    time.sleep(0.5 - ((time.time() - starttime) % 0.5))

    