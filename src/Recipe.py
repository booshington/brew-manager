import json
import logging
from typing import List

from src.Grain import Grain
from src.Hop import Hop

logger = logging.getLogger("main")


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
        logger.debug("Building Recipe object for: %s" % json_input)
        return Recipe(
            name=json_input["name"],
            grains=json_input["grains"],
            hops=json_input["hops"],
        )

    @classmethod
    def dump_to_json(self):
        pass

    def __repr__(self):
        return self.name

    def __dict__(self):
        hops = []
        for hop in self.hops:
            hops.append(hop.__dict__())
        grains = []
        for grain in self.grains:
            grains.append(grain.__dict__())
        return {"name": self.name, "grains": grains, "hops": hops}
