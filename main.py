
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


while True:
    app.render()
    # Remove the Time taken by code to execute
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))