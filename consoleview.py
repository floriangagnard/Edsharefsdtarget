

from context import Context
import os
import time

from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.markdown import Markdown


class ConsoleView:
    def __init__(self,context: Context ) -> None:
        self.context = context 

    def render(self):
        os.system('cls')
        table = Table()
        table.add_column("")
        table.add_column("Cible")
        table.add_column("Position")
        console = Console(width=150,height=100)
        commanderview = Panel(self.get_content(self.context.crew.commander), expand=True, height=6  )
        user_renderables = [Panel(self.get_content(user), expand=True, height=6  ) for user in self.context.crew.wingmen]
        console.print(commanderview)
        console.print(Columns([Columns(user_renderables,width = 50, title ="wingmen"), Columns([Markdown(self.build_log(self.context.logDataApp))],expand =True,  title ="Logs",align ="left")],width=70))
        #console.print(Columns([Columns(user_renderables), Text("style")]))
       #with Live(table, refresh_per_second=1):  # update 4 times a second to feel fluid
        #    for user in self.context.crew.wingmen:
         #       table.add_row(f"{user.name}", f" Cible     :{user.target}", f"[red] Position :{user.position}")

    
    def get_content(self,commander):
        """Extract text from user dict."""
        
        return f"[b]{commander.name}[/b]\n Cible FSD : [yellow]{commander.target}\n [white]Position : [yellow]{commander.position}" 
    
    def build_log(self,logs):
        """Extract text from user dict."""
        string = ""
        for log in logs:
            string = string + "\n * " + log
        return string    
        