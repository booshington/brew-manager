import logging
from tkinter import Tk, Frame, filedialog, Label, Button, Listbox
import json
from typing import List
import time

from src.Recipe import Recipe
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("main")

recipe_db = []

def load_recipe_json(recipe_list: Listbox):
    filename = filedialog.askopenfilename(initialdir = "~/workspace/brew-manager/test_recipes",
        title = "Select a File",
        filetypes = (("JSON files", "*.json*"), ("all files", "*.*")))
    with open(filename) as j_file:
        data: List[Listbox] = json.load(j_file)

    for recipe in data:
        recipe = Recipe.load_from_json(recipe)
        recipe_db.append(recipe)
        recipe_list.insert("end", recipe)

    recipe_list.pack()

def export_recipe(recipe: Recipe):
    logger.warning("Exporting recipe")
    logger.warning(recipe.__dict__())
    export_filename = "recipe_export_%s.json" % time.time()
    with open(file=export_filename, mode='x') as f:
        json.dump([recipe.__dict__()], f, ensure_ascii=False, indent=4)
