import json

def load_json_file(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)