import logging
from tkinter import Tk, Frame, filedialog, Label, Button, Listbox
import json
from typing import List
import time
import os

from src.Recipe import Recipe
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("main")

recipe_db = []

def open_recipe_json(recipe_list: Listbox, j_filename: list = []):
    '''
        Queries the user for a json file and loads the recipes into application
    '''
    if not j_filename:
        j_filename = filedialog.askopenfilename(initialdir=os.getcwd()+"/test_recipes", title = "Select a File",
            filetypes = (("JSON files", "*.json*"), ("all files", "*.*")))
    
    with open(j_filename) as j_file:
        data: List[dict] = json.load(j_file)

    for recipe in data:
        load_recipe(recipe_list, recipe)

    recipe_list.pack()

def load_recipe(recipe_list: Listbox, recipe: dict):
    logging.warning("recipe type: %s" % type(recipe))
    recipe = Recipe.load_from_json(recipe)
    recipe_db.append(recipe)
    recipe_list.insert("end", recipe)

def export_recipe(recipe: Recipe):
    logger.warning("Exporting recipe")
    logger.warning(recipe.__dict__())
    export_filename = "recipe_export_%s.json" % time.time()
    with open(file=export_filename, mode='x') as f:
        json.dump([recipe.__dict__()], f, ensure_ascii=False, indent=4)
