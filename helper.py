from datetime import date
import json

class Datahelper():
    def __init__(self, filename):
        self.filename = filename
        self.data = self.parse_json()

    def parse_json(self):
        try:
            with open(self.filename, "r+") as file:
                data = json.load(file)
        except:
            return ""
        else:
            return data

    def get_data(self):
        return self.data
    
    def __repr__(self) -> str:
        return 'Data Object: "{}"'.format(self.filename)

