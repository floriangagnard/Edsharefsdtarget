import json
import requests
from crew import Crew

class Context:
    def __init__(self,  crew : Crew):
        self.crew = crew
        self.logDataApp = []
    def serialize(self):
        """
        Methode permettantde serialiser l'instance du crew en json
        """
        return  json.dumps(self, indent=4, default=lambda o: o.__dict__)
    
    def action_publish_target(self):
        # to EDSM 
        commander = self.crew.commander
        try:
            params = {
                "commanderName": commander.name,
                "apiKey": commander.key,
                "systemName": "sol",
                "comment": commander.target
            }

            url = "https://www.edsm.net/api-logs-v1/set-comment"
            response = requests.get(url, params=params)

            # response JSON
            if response.status_code == 200:
                data = response.json()
                if data['msgnum'] == 100:
                   
                    self.add_to_logs(f"Commentaire ajouté avec succès.")
                else:
                    self.add_to_logs(f"Erreur lors de l'ajout du commentaire : {data['msg']}")
            else:
                self.add_to_logs(f"Erreur lors de la requête à l'API EDSM. Code de statut : {response.status_code}")

        except Exception as e:
            self.add_to_logs(f"Une erreur s'est produite : {str(e)}")


    def action_publish_targetV2(self):
        # to EDSM 
        commander = self.crew.commander
        self.add_to_logs(f"**Info** BroadCast: {commander.target}")
        try:

            for innerWingmen in self.crew.wingmen:
                if innerWingmen.connector !=  "": 
                    url = f'{innerWingmen.connector}/wingmen/{commander.name}/target/{commander.target}'
                    # do something with v
                
                    response = requests.post(url)

                    # response JSON
                    if response.status_code == 200:
                        self.add_to_logs(f"Update.")
                    else:
                        self.add_to_logs(f"**W** Erreur lors de la requête à l'API EDSM. Code de statut : {response.status_code}")
                else:
                    self.add_to_logs(f"**Warn** No BroadCast adress for: {innerWingmen.name}")

        except Exception as e:
            self.add_to_logs(f"Une erreur s'est produite : {str(e)}")
        
    def add_to_logs(self,log: str):
        if len(self.logDataApp) > 19 :
            
            del self.logDataApp[0]
                
            
        self.logDataApp.append(log)