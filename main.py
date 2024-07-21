import tkinter.ttk as ttk
from tkinter import Tk, Frame, Label, Button, Listbox
import json
import logging

from src.Recipe import Recipe
from src.util import open_recipe_json, recipe_db, export_recipe

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main")

def main():
    # Create the main window
    window_root = Tk()
    window_root.geometry("500x700") #TODO: move to config
    window_root.title("Brew Manager v0.1")

    # Create a notebook (tab control)
    notebook = ttk.Notebook(window_root)
    tab_recipe_manager = Frame(notebook)
    tab_recipe_builder = Frame(notebook)
    tab_recipe_viewer = Frame(notebook)

    #Add tabs to Notebook
    notebook.add(tab_recipe_manager, text='Recipe Manager')
    notebook.add(tab_recipe_viewer, text='Recipe Viewer')
    notebook.add(tab_recipe_builder, text='Recipe Builder')

    #Tab Title
    recipe_label = Label(tab_recipe_manager, text="Current Recipes:")
    recipe_label.pack()

    #Recipe List
    recipe_list = Listbox(tab_recipe_manager)

    def recipe_activate(event):
        logger.info("Recipe activated, loading...")
        recipe_index,  = recipe_list.curselection()
        # I hope this doesn't break
        selected_recipe = recipe_db[recipe_index]
        logger.info("Selected Recipe: %s" % selected_recipe)
        logger.info(recipe_db)
        export_recipe(selected_recipe)


    recipe_list.bind('<Double-1>', recipe_activate) 

    #TODO: Use a Frame object to reorient Button objects
    button_explore = Button(tab_recipe_manager, text = "Load Recipes", command=lambda: open_recipe_json(recipe_list)) 
    button_exit = Button(tab_recipe_manager, text = "Exit", command = exit)
    button_explore.pack()
    button_exit.pack()  

    # Add the notebook to the window_root window
    notebook.pack(expand=True, fill='both')

    logger.info("Running mainloop...")

    # Run the application
    window_root.mainloop()

if __name__ == "__main__":
    main()