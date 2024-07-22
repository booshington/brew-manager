import tkinter.ttk as ttk
from tkinter import Tk, Frame, Listbox
import logging

from src.util import recipe_db
from src.ui.recipe_manager import build_recipe_manager
from src.ui.recipe_builder import build_recipe_builder

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

    #Add tabs to Notebook
    notebook.add(tab_recipe_manager, text='Recipe Manager')
    notebook.add(tab_recipe_builder, text='Recipe Builder')

    #Recipe List
    recipe_list = Listbox(tab_recipe_manager)

    build_recipe_manager(tab_recipe_manager, recipe_list)
    build_recipe_builder(tab_recipe_builder, window_root, recipe_list, recipe_db)
    # Add the notebook to the window_root window
    notebook.pack(expand=True, fill='both')

    logger.info("Running mainloop...")
    # Run the application
    window_root.mainloop()

if __name__ == "__main__":
    main()