import tkinter as tk
import tkinter.ttk as ttk
from math import sqrt

def calculate_sqrt():
    try:
        num = float(entry.get())
        result = sqrt(num)
        output_label.config(text=f"The square root is: {result}")
    except ValueError:
        output_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Tabbed Interface Example")

# Create a notebook (tab control)
notebook = ttk.Notebook(root)

# First tab: Input and Calculate Square Root
tab1 = tk.Frame(notebook)
notebook.add(tab1, text='Square Root')

# Add widgets to the first tab
label = tk.Label(tab1, text="Enter a number:")
label.pack(pady=5)

entry = tk.Entry(tab1)
entry.pack(pady=5)

submit_button = tk.Button(tab1, text="Calculate", command=calculate_sqrt)
submit_button.pack(pady=5)

output_label = tk.Label(tab1, text="")
output_label.pack(pady=10)

# Add the notebook to the root window
notebook.pack(expand=True, fill='both')

# Run the application
root.mainloop()
