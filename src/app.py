# app.py
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from resources import *
from random import choice, randint

app = Flask(__name__)
api = Api(app)

npcs = [
    {"id": 1, "name": "Hans", "race": "human", "career": "merchant"},
    {"id": 2, "name": "Torsten", "race": "human", "career": "townsman"},
    {"id": 3, "name": "Karl", "race": "human", "career": "guard"}
]

class NPC(Resource):
    def get(self):
        return {
            
        }

def generate_name():
    return f"{choice(male_reiklander)} {choice(reiklander_surname)}"

def generate_career():
    return human_careers[randint(0, 100)]

def get_class(career):
    if career in academics: return "academic"
    elif career in burghers: return "burgher"
    elif career in courtiers: return "courtier"
    elif career in peasants: return "peasant"
    elif career in rangers: return "ranger"
    elif career in riverfolk: return "riverfolk"
    elif career in rogues: return "rogue"
    elif career in warriors: return "warrior"

def _find_next_id():
    return max(npc["id"] for npc in npcs) + 1

@app.route("/burgher", methods=["GET"])
def get_burgher():
    npc = {"id": _find_next_id(),"name": generate_name(), "race":"human", "career": choice(burghers)}
    npcs.append(npc)
    return npc

@app.route("/allnpcs", methods = ["GET"])
def get_all():
    return jsonify(npcs)

@app.route("/create_npcs/<amount>")
def create_npcs(amount):
    generated_npcs = []
    
    for _ in range(int(amount)):
        this_npc = {}
        this_npc["name"] = generate_name()
        this_npc["career"] = generate_career()
        this_npc["class"] = get_class(this_npc["career"])
        
        generated_npcs.append(this_npc)
    
    return jsonify(generated_npcs)
"""
@app.post("/addnpc")
def add_chosen_npc():
    if request.is_json:
        npc = request.get_json()
        npc["name"] = _find_next_id()
        npcs.append(npc)
        return npc, 201 # ID: Created
    return {"error": "Request must be JSON"}, 415 # ID: Unsupported Media Type
"""

@app.route("/")
def home():
    return "<h1>Welcome to the NPC generator of Reikland!</h1>"

if __name__ == '__main__':
    app.run(debug=True)