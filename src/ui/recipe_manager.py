from tkinter import Frame, Label, Button, Listbox
import logging

from src.Recipe import Recipe
from src.util import open_recipe_json, export_selected_recipe, recipe_db

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("main")


def build_recipe_manager(tab_recipe_manager: Frame, recipe_list: Listbox):
    # Tab Title
    recipe_label = Label(tab_recipe_manager, text="Current Recipes:")
    recipe_label.pack()

    def recipe_activate(event):
        logger.warning("Recipe activated")
        (recipe_index,) = recipe_list.curselection()
        # I hope this doesn't break
        selected_recipe: Recipe = recipe_db[recipe_index]
        logger.warning(selected_recipe)
        # TODO: Formatting
        recipe_viewer.configure(text=selected_recipe.__dict__())

    recipe_list.bind("<Double-1>", recipe_activate)

    # TODO: Use a Frame object to reorient Button objects
    button_explore = Button(
        tab_recipe_manager,
        text="Load Recipes",
        command=lambda: open_recipe_json(recipe_list),
    )
    button_export = Button(
        tab_recipe_manager,
        text="Export Selected Recipe",
        command=lambda: export_selected_recipe(recipe_list),
    )
    button_explore.pack()
    button_export.pack()

    recipe_viewer = Label(tab_recipe_manager, text="asdf")
    recipe_viewer.pack()
