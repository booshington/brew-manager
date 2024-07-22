import json


class Grain:
    name: str
    weight: float
    srm: float

    def __init__(self, name, weight, srm):
        self.name = name
        self.weight = weight
        self.srm = srm

    @classmethod
    def load_from_json(cls, json_input: json):
        return Grain(
            name=json_input["name"], weight=json_input["weight"], srm=json_input["srm"]
        )

    def __repr__(self):
        return self.name

    def __dict__(self):
        return {"name": self.name, "weight": self.weight, "srm": self.srm}

    def to_str(self):
        return self.name
