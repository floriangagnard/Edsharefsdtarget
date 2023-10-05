import tkinter as tk
import subprocess
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import configAndData
import log_monitor
import api_interaction
import pyperclip
import pyttsx3

import threading

#from multiprocessing import Process, freeze_support  # Importez freeze_support
voice_enabled = False

from tkinter import ttk

def start_log_monitor():
    log_monitor_thread = threading.Thread(target=log_monitor.run_log_monitor)
    log_monitor_thread.daemon = True  # Le thread se terminera lorsque l'application principale se terminera
    log_monitor_thread.start()

last_wingman1_fsdtarget_value = None

## synthèse vocale
engine = pyttsx3.init()
text_to_speak = "New suggested FSD Target acquired : "
##

class JSONFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "config_and_data.json":
            update_labels()

############# new windows de config ####################


def open_config_window():
    config_window = tk.Toplevel(main_window)
    config_window.title("Configuration")

    with open("config_and_data.json", "r") as json_file:
        config_data = json.load(json_file)

    label_your_cmd_name = ttk.Label(config_window, text="Your CMD NAME:")
    label_your_cmd_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entry_your_cmd_name = ttk.Entry(config_window, width=30)
    entry_your_cmd_name.grid(row=0, column=1, padx=10, pady=5)
    entry_your_cmd_name.insert(0, config_data["my_commander"]["name"])

    label_your_apikey = ttk.Label(config_window, text="Your apikey :")
    label_your_apikey.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    entry_your_apikey = ttk.Entry(config_window, width=30)
    entry_your_apikey.grid(row=1, column=1, padx=10, pady=5)
    entry_your_apikey.insert(0, config_data["my_commander"]["api_key"])

    label_wingman1_name = ttk.Label(config_window, text="Wingman 1 CMD NAME:")
    label_wingman1_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    entry_wingman1_name = ttk.Entry(config_window, width=30)
    entry_wingman1_name.grid(row=2, column=1, padx=10, pady=5)
    entry_wingman1_name.insert(0, config_data["wingman1"]["name"])

    label_wingman1_apikey = ttk.Label(config_window, text="Wingman 1 apikey:")
    label_wingman1_apikey.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    entry_wingman1_apikey = ttk.Entry(config_window, width=30)
    entry_wingman1_apikey.grid(row=3, column=1, padx=10, pady=5)
    entry_wingman1_apikey.insert(0, config_data["wingman1"]["api_key"])


    def save_config_data():
        config_data["my_commander"]["name"] = entry_your_cmd_name.get()
        config_data["my_commander"]["api_key"] = entry_your_apikey.get()
        config_data["wingman1"]["name"] = entry_wingman1_name.get()
        config_data["wingman1"]["api_key"] = entry_wingman1_apikey.get()

        with open("config_and_data.json", "w") as json_file:
            json.dump(config_data, json_file, indent=4)
        
        config_window.destroy()

    # Bouton enregistrer 
    save_button = ttk.Button(config_window, text="Enregistrer", command=save_config_data)
    save_button.grid(row=5, column=0, columnspan=2, pady=10)


################## fin  new window ###################

def update_labels():
    with open("config_and_data.json", "r") as json_file:
        config_data = json.load(json_file)

    labels_data = [
        ("Your CMR name: ", config_data["my_commander"]["name"]),
        ("Your current system: ", config_data["my_commander"]["current_StarSystem"]),
        ("Last target name: ", config_data["my_commander"]["FSDTarget"]),
        ("--------------------"),
        ("Wingman1 name: ", config_data["wingman1"]["name"]),
        ("Wingman's current system: ", config_data["wingman1"]["current_StarSystem"]),
        ("Wingman's FSDTarget: ", config_data["wingman1"]["FSDTarget"]),
        ("--------------------"),
    ]

    for label, value in zip(labels, labels_data):
        label.config(text=f"{value[0]}{value[1]}")

    main_window.after(1000, update_labels)

main_window = tk.Tk()
main_window.geometry("400x330")
main_window.title("Wingman's FSDtarget detector")

police = (24)
config_button = tk.Button(main_window, text="⚙️", command=open_config_window)
config_button.pack(side=tk.TOP)

labels = []
for _ in range(8):
    label = tk.Label(main_window, font=police)
    label.pack()
    labels.append(label)







def copy_wingman1_FSDTarget(wingman1_FSDTarget, autocopy=False):
    if wingman1_FSDTarget != "":
        pyperclip.copy(wingman1_FSDTarget)
        if autocopy:
            pyperclip.copy(wingman1_FSDTarget)
            if voice_toggle_state.get():  # Vérifiez si la synthèse vocale est activée
                engine.say(text_to_speak + wingman1_FSDTarget)
                engine.runAndWait()


def get_wingman1_data():
    global wingman1_FSDTarget
    global last_wingman1_fsdtarget_value
    if toggle_state.get():
        with open("config_and_data.json", "r") as json_file:
            config_data = json.load(json_file)

        wingman_commander_name = config_data["wingman1"]["name"]
        wingman_api_key = config_data["wingman1"]["api_key"]
        api_interaction.get_wingman_current_StarSystem(wingman_commander_name, wingman_api_key)
        #api_interaction.get_wingman_comment(wingman_commander_name, wingman_api_key)
        wingman1_FSDTarget = api_interaction.get_wingman_comment(wingman_commander_name, wingman_api_key)
        
        if copy_toggle_state.get() and wingman1_FSDTarget != last_wingman1_fsdtarget_value:
            copy_wingman1_FSDTarget(wingman1_FSDTarget, True)
            last_wingman1_fsdtarget_value = wingman1_FSDTarget

        # a modifer si update à l'api trop fréquent 
        main_window.after(10000, get_wingman1_data)
    else:
        main_window.after_cancel(get_wingman1_data)

def toggle_update():
    if toggle_state.get():
        # a modifer si update à l'api trop fréquent 
        main_window.after(10000, get_wingman1_data)
        copy_toggle_button.config(state=tk.NORMAL)
        copy_button.config(state=tk.NORMAL)
    else:
        main_window.after_cancel(get_wingman1_data)
        copy_toggle_button.config(state=tk.DISABLED) 
        copy_button.config(state=tk.DISABLED)


voice_toggle_state = tk.BooleanVar(value=voice_enabled)
voice_toggle_button = tk.Checkbutton(main_window, text="Enable voice info", variable=voice_toggle_state)
voice_toggle_button.pack()


toggle_state = tk.BooleanVar(value=False)
toggle_button = tk.Checkbutton(main_window, text="Toggle update wingman's info", variable=toggle_state, command=toggle_update)
toggle_button.pack()

copy_toggle_state = tk.BooleanVar(value=False)
copy_toggle_button = tk.Checkbutton(main_window, text="Autocopy fsdtarget to Clipboard if new", variable=copy_toggle_state)
copy_toggle_button.config(state=tk.DISABLED)
copy_toggle_button.pack()

copy_button = tk.Button(main_window, text="Copy Wingman1 FSDTarget", command=lambda: copy_wingman1_FSDTarget(wingman1_FSDTarget, False), font=("", 15))
copy_button.config(state=tk.DISABLED)
copy_button.pack()



get_wingman1_data()




################    TEST ZONE   ###################
#todo ? : sendtoapi(my_commander_name, my_api_key, current_StarSystem,FSDTarget)

####################   END TEST ZONE   ######################


update_labels()
start_log_monitor()


# gestion de l'observateur
observer = Observer()
directory_to_watch = "."
observer.schedule(JSONFileHandler(), directory_to_watch)
observer.start()

main_window.mainloop()



# stop l'observateur
observer.stop()
observer.join()

