import json
from typing import List

from src.Grain import Grain
from src.Hop import Hop

class Recipe:
    name: str
    grains: List[Grain] = []
    hops: List[Hop] = []

    def __init__(self, name: str, grains: List, hops: List):
        self.name = name
        for grain in grains:
            self.grains.append(Grain.load_from_json(grain))
        for hop in hops:
            self.hops.append(Hop.load_from_json(hop))

    @classmethod
    def load_from_json(cls, json_input: json):
        return Recipe(
            name=json_input["name"],
            grains=json_input["grains"],
            hops=json_input["hops"]
        )

    def __repr__(self):
        return self.name