import tkinter.ttk as ttk
from tkinter import Tk, Frame, filedialog, Label, Button, Listbox
import json
import logging

from Recipe import Recipe

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main")

def main():
    #TODO: refactor
    def load_recipe_json():
        filename = filedialog.askopenfilename(initialdir = "~/workspace/brew-manager/test_recipes",
            title = "Select a File",
            filetypes = (("JSON files", "*.json*"), ("all files", "*.*")))
        with open(filename) as j_file:
            data = json.load(j_file)
        
        #Add recipe to list
        recipe = Recipe.load_from_json(data)
        recipe_list.insert("end", recipe)
        recipe_list.pack()

    # Create the main window
    window_root = Tk()
    window_root.geometry("500x700") #TODO: move to config
    window_root.title("Brew Manager v0.1")
    # Create a notebook (tab control)
    notebook = ttk.Notebook(window_root)
    # First tab: Recipe Manager
    tab_recipe_manager = Frame(notebook)
    # Second tab: Recipe Builder
    tab_recipe_builder = Frame(notebook)
    #Add tabs to Notebook
    notebook.add(tab_recipe_manager, text='Recipe Manager')
    notebook.add(tab_recipe_builder, text='Recipe Builder')

    #Tab Title
    recipe_label = Label(tab_recipe_manager, text="Current Recipes:")
    recipe_label.pack()

    #Recipe List
    recipe_list = Listbox(tab_recipe_manager)

    #TODO: refactor
    def go(event):
        logger.info(recipe_list.get(recipe_list.curselection()))

    recipe_list.bind('<Double-1>', go) 

    #TODO: Use a Frame object to reorient Button objects
    button_explore = Button(tab_recipe_manager, text = "Load Recipe", command = load_recipe_json) 
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