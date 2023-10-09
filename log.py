
import json
class LogEntry ():
    def __init__(self,timestamp,event,name="", star_system="") -> None:
        self.timestamp = timestamp
        self.event = event
        self.name = name
        self.star_system = star_system

    @staticmethod
    def deserialize(json_string : str ) :
        """
        Methode statique permettant de creer une instance de commander à partir d'une string JSON
        """
        myjson = json.loads(json_string)
        lgo =  LogEntry(timestamp=myjson['timestamp'],event = myjson['event'])
        if 'Name' in myjson:
            lgo.name= myjson['Name']    
        if 'StarSystem' in myjson:
            lgo.star_system= myjson['StarSystem']        
        return lgo
        


# FSDTarget 
# {"timestamp":"2023-10-09T11:50:25Z","event":"SupercruiseExit","Taxi":false,"Multicrew":false,"StarSystem":"Scheau Pri ZC-T c4-158","SystemAddress":43505434306090,"Body":"Scheau Pri ZC-T c4-158 10","BodyID":35,"BodyType":"Planet"}
# {"timestamp":"2023-10-09T11:51:57Z","event":"SupercruiseEntry","Taxi":false,"Multicrew":false,"StarSystem":"Scheau Pri ZC-T c4-158","SystemAddress":43505434306090}