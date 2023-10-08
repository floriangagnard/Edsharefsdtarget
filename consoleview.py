

from context import Context
import os

class ConsoleView:
    def __init__(self,context: Context ) -> None:
 
        self.context = context 
    def render(self):
        os.system('cls')
        print(self.context.crew.commander.to_string())

        print(self.context.crew.wingmen[0].to_string())
        print(self.context.crew.wingmen[1].to_string())
        for innerLog in self.context.logDataApp:
            print(innerLog)