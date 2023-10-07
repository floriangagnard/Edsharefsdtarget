
import time
starttime = time.time()

from crew import Crew
from commander import Commander
import dataStorageService
from interface import App



## Initilisation du Commander
mainCommander = dataStorageService.read_main_commander()
listWingMan = dataStorageService.read_wingmens_commanders()
crew = Crew(mainCommander,listWingMan)


app = App(crew= crew)


app.mainloop()