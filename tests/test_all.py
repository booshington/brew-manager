import unittest
import logging
from tkinter import Tk, Frame, filedialog, Label, Button, Listbox

from src.util import export_recipe, load_recipe
from src.Recipe import Recipe

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main")

test_recipe_json = {
    "name":"Silly Lil' Guy",
    "grains":[
        {
            "name":"2-row",
            "weight":10.0,
            "srm":"1.0"
        },
        {
            "name":"Roasted Barley",
            "weight":5.0,
            "srm":"100.0"
        }
    ],
    "hops":[
        {
            "name":"Cascade",
            "aa":"",
            "weight":2.0,
            "time":60
        }
    ]
}

test_recipe = Recipe(**test_recipe_json)
test_listbox = Listbox()

class TestRecipes(unittest.TestCase):

    def test_nothing(self):
        assert True

    def test_recipe_export(self):
        export_recipe(test_recipe)

    def test_load_recipe(self):
        load_recipe(recipe_list=test_listbox, recipe=test_recipe_json)

if __name__ == '__main__':
    unittest.main()