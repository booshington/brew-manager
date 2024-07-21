import tkinter.ttk as ttk
from tkinter import Tk, Frame, filedialog, Label, Button
from math import sqrt
import json


def load_recipe_json():
    filename = filedialog.askopenfilename(initialdir = "/",
        title = "Select a File",
        filetypes = (("JSON files", "*.json*"), ("all files", "*.*")))
    
    with open(filename) as j_file:
        data = json.load(j_file)

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    recipe_label.configure(text=data)

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

# with open("recipe.json") as j_file:
#     data = json.load(j_file)

# Add widgets to the first tab
recipe_label = Label(tab_recipe_manager, text="")
recipe_label.pack()

label_file_explorer = Label(tab_recipe_manager, 
    text = "File Explorer using Tkinter",
    # width = 100, height = 4, 
    fg = "blue")

button_explore = Button(tab_recipe_manager, 
    text = "Load Recipe",
    command = load_recipe_json) 
button_exit = Button(tab_recipe_manager, 
    text = "Exit",
    command = exit) 
label_file_explorer.pack()
button_explore.pack()
button_exit.pack()

# entry = tk.Entry(tab_recipe_manager)
# entry.pack(pady=5)

# submit_button = tk.Button(tab_recipe_manager, text="Calculate", command=calculate_sqrt)
# submit_button.pack(pady=5)

# output_label = tk.Label(tab_recipe_manager, text="")
# output_label.pack(pady=10)

# Create a File Explorer label

  

# Add the notebook to the window_root window
notebook.pack(expand=True, fill='both')

# Run the application
window_root.mainloop()
