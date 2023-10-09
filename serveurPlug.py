from flask import Flask, jsonify
from context import Context
from commanders import Commanders



def create_application(app_name, context: Context):

    app = Flask(app_name)

    #cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route("/informations", methods=["POST", "GET", "OPTION"])
    def ping():
        try:
            context.add_to_logs("ping")
            return context.crew.commander.serialize()
        except Exception as e:
             context.add_to_logs("ping KO")

    @app.route("/wingmen/<name>", methods=["POST", "GET", "OPTION"])
    def commanders(name):
        context.add_to_logs(f"lecture du wingmen {name}")
        try:
            commander = Commanders.findByName(context.crew.wingmen,name)
            if commander == None :
                response = jsonify({'status': 404,'error': 'not found',
                        'message': 'invalid resource URI'})
                response.status_code = 404
                return response
            context.add_to_logs(name)
            return commander.serialize()
        except Exception as e:
            context.add_to_logs(e)
            return e.with_traceback
        
    @app.route("/wingmen/<name>/position/<position>", methods=["POST"])
    def update_commander_position(name,position):
        context.add_to_logs(f"RECEPTION d'un position {position} pour le commander {name}")
        try:
            commander = Commanders.findByName(context.crew.wingmen,name)
            if commander == None :
                response = jsonify({'status': 404,'error': 'not found',
                        'message': 'invalid resource URI'})
                response.status_code = 404
                return response
            commander.position=position
            
            return commander.serialize()
        except Exception as e:
            context.add_to_logs("ping KO")
           
            return e
        

    @app.route("/wingmen/<name>/target/<target>", methods=["POST"])
    def update_commander_target(name,target):
        context.add_to_logs(f"RECEPTION d'un cible {target} pour le commander {name}")
        try:
            commander = Commanders.findByName(context.crew.wingmen,name)
            if commander == None :
                response = jsonify({'status': 404,'error': 'not found',
                        'message': 'invalid resource URI'})
                response.status_code = 404
                return response
            commander.target=target
            
            return commander.serialize()
        except Exception as e:
             context.add_to_logs("ping KO")
             return e
        
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers",
                             "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods",
                             "GET,PUT,POST,DELETE,OPTIONS")
        return response

    app.run(port=7000)
