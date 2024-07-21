from tkinter import Tk, Frame, filedialog, Label, Button, Listbox
import json

from src.Recipe import Recipe

recipe_db = []

def load_recipe_json(recipe_list: Listbox):
    filename = filedialog.askopenfilename(initialdir = "~/workspace/brew-manager/test_recipes",
        title = "Select a File",
        filetypes = (("JSON files", "*.json*"), ("all files", "*.*")))
    with open(filename) as j_file:
        data = json.load(j_file)
    
    recipe = Recipe.load_from_json(data)

    recipe_db.append(recipe)
    
    recipe_list.insert("end", recipe)
    recipe_list.pack()