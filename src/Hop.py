import json
import logging

logger = logging.getLogger("main")



class Hop:
    name: str
    weight: float
    aa: float
    time: float

    def __init__(self, name, weight, aa, time):
        self.name = name
        self.weight = weight
        self.aa = aa
        self.time = time

    @classmethod
    def load_from_json(cls, json_input: json):
        return Hop(
            name=json_input["name"],
            weight=json_input["weight"],
            aa=json_input["aa"],
            time=json_input["time"]
        )

    def __repr__(self):
        return self.name
    
    def __dict__(self):
        return {
            "name":self.name,
            "weight":self.weight,
            "aa":self.aa,
            "time":self.time
        }
    
    def to_str(self):
        return self.name