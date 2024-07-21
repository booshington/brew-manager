import logging
from tkinter import Tk, Frame, filedialog, Label, Button, Listbox
import json
from typing import List

from src.Recipe import Recipe

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