import customtkinter
from crew import Crew
from commander import Commander

class App(customtkinter.CTk):
    def __init__(self, crew: Crew):
        super().__init__()
        self.geometry("800x600")
        self.crew = crew
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_rowconfigure(1, weight=10)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        
        self.title_frame = TitleFrame(master=self)
        self.title_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew",  columnspan=2)

        self.commanderFrame = CommanderFrame(commander = crew.commander ,master=self)
        self.commanderFrame.grid(row=1, column=0,padx=5, pady=5,sticky="nsew")

        self.WingMenFrame = WingMenFrame(master=self)
        self.WingMenFrame.grid(row=1, column=1,padx=5, pady=5,sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="refresh", command=self.refresh_window )
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="nsew",  columnspan=2) 

    def refresh_window(self):
        # Redraw the window
        self.update()
        self.update_idletasks()
        print(f"Refresh completed.{self.crew.commander.name}")



class TitleFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.fg_color=("#DB3E39", "#821D1A")
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="Wingman's FSDtarget detector", fg_color=("#DB3E39", "#821D1A"), font=('',25)) 
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

      

class CommanderFrame(customtkinter.CTkFrame):
    def __init__(self, master,commander:Commander,  **kwargs):
        super().__init__(master, **kwargs)
        self.fg_color=("#DB3E39", "#821D1A")
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text=commander.name, fg_color=("#DB3E39", "#821D1A"), font=('',25)) 
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.button = customtkinter.CTkButton(self, text="test", command=lambda: buttonaction("vincent", commander))
        self.button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew") 

def buttonaction(name,commander):
    commander.name = name
    print(f"change {commander.name}")

    

class WingMenFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.fg_color=("#DB3E39", "#821D1A")
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="test", fg_color=("#DB3E39", "#821D1A"), font=('',25)) 
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")