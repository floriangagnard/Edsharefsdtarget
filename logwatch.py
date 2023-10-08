
import os 
from watchdog.events import FileSystemEventHandler

windows_username = os.getlogin()
path = os.path.join("C:\\", "Users", windows_username, "Saved Games", "Frontier Developments", "Elite Dangerous")


class LogEDFile(FileSystemEventHandler):
    def __init__(self, context , callback) -> None:
        super().__init__()
        self.callback = callback
        self.context = context

    def on_modified(self, event):
        self.callback(self.context, event.event_type, event.src_path)
            