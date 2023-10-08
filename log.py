
import json
class LogEntry ():
    def __init__(self,timestamp,event,name) -> None:
        self.timestamp = timestamp
        self.event = event
        self.name = name

    @staticmethod
    def deserialize(json_string : str ) :
        """
        Methode statique permettant de creer une instance de commander à partir d'une string JSON
        """
        myjson = json.loads(json_string)
        return LogEntry(timestamp=myjson['timestamp'],event = myjson['event'],name= myjson['Name'])


# FSDTarget