import json


class Hop:
    name: str
    weight: float
    aa: float
    time: float

    def __init__(self, name, weight, aa, time):
        self.name = name
        self.weight = weight
        self.aa = aa
        self.time: time

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