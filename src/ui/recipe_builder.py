import logging
from tkinter import Tk, Frame, Label, Button, Listbox, Entry, StringVar, Toplevel
from typing import List

from src.Grain import Grain
from src.Hop import Hop
from src.Recipe import Recipe

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("main")


def show_add_hops_window(window_root, hop_list, hop_db):
    top = Toplevel(window_root)
    top.geometry("250x750")
    Label(top, text="Hop Entry:", font=("Mistral", 18, "bold")).pack()

    name_var = StringVar()
    weight_var = StringVar()
    time_var = StringVar()
    aa_var = StringVar()

    Label(top, text="Name: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=name_var, font=("calibre", 10, "normal")).pack()
    Label(top, text="Weight: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=weight_var, font=("calibre", 10, "normal")).pack()
    Label(top, text="Time: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=time_var, font=("calibre", 10, "normal")).pack()
    Label(top, text="AA %: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=aa_var, font=("calibre", 10, "normal")).pack()

    def save_hops():
        name = name_var.get()
        weight = weight_var.get()
        time = time_var.get()
        aa = aa_var.get()

        logger.debug("Adding new hop: %s %s %s %s" % (name, weight, time, aa))
        hop = Hop(name=name, weight=weight, time=time, aa=aa)
        hop_list.insert("end", hop)
        hop_db.append(hop)

        name_var.set("")
        weight_var.set("")
        time_var.set("")
        aa_var.set("")

    Button(top, text="Add Hop", command=save_hops).pack()


def show_add_grain_window(window_root, grain_list, grain_db):
    top = Toplevel(window_root)
    top.geometry("250x750")
    Label(top, text="Grain Entry:", font=("Mistral", 18, "bold")).pack()

    name_var = StringVar()
    weight_var = StringVar()
    srm_var = StringVar()

    Label(top, text="Name: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=name_var, font=("calibre", 10, "normal")).pack()
    Label(top, text="Weight: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=weight_var, font=("calibre", 10, "normal")).pack()
    Label(top, text="SRM: ", font=("calibre", 10, "bold")).pack()
    Entry(top, textvariable=srm_var, font=("calibre", 10, "normal")).pack()

    def save_grain():
        name = name_var.get()
        weight = weight_var.get()
        srm = srm_var.get()

        logger.debug("Adding new grain: %s %s %s" % (name, weight, srm))
        grain = Grain(name=name, weight=weight, srm=srm)
        grain_list.insert("end", grain)
        grain_db.append(grain)

        name_var.set("")
        weight_var.set("")
        srm_var.set("")

    Button(top, text="Add Grain", command=save_grain).pack()


def build_recipe_builder(
    tab_recipe_builder: Frame,
    window_root: Tk,
    recipe_list: Listbox,
    recipe_db: List[Recipe],
):
    name_var = StringVar()

    grain_list = Listbox(tab_recipe_builder)
    grain_db: List[Grain] = []
    hop_list = Listbox(tab_recipe_builder)
    hop_db: List[Hop] = []

    def save_recipe():
        name = name_var.get()
        grains = []
        hops = []
        logger.warning("Loading Grains")
        for count, value in enumerate(grain_db):
            logger.warning(value)
            grains.append(value.__dict__())
        logger.warning("Loading Hops")
        for count, value in enumerate(hop_db):
            logger.warning(value)
            hops.append(value.__dict__())

        recipe = Recipe(name=name, grains=grains, hops=hops)
        logger.warning(recipe)
        recipe_list.insert("end", recipe)
        recipe_db.append(recipe)
        recipe_list.pack()

    # Recipe Name
    Label(tab_recipe_builder, text="Name: ", font=("calibre", 10, "bold")).pack()
    Entry(
        tab_recipe_builder, textvariable=name_var, font=("calibre", 10, "normal")
    ).pack()

    # View current recipe state
    Label(tab_recipe_builder, text="Grains: ", font=("calibre", 10, "bold")).pack()
    grain_list.pack()
    Label(tab_recipe_builder, text="Hops: ", font=("calibre", 10, "bold")).pack()
    hop_list.pack()

    Button(
        tab_recipe_builder,
        text="Add Grain",
        command=lambda: show_add_grain_window(
            window_root=window_root, grain_list=grain_list, grain_db=grain_db
        ),
    ).pack()
    Button(
        tab_recipe_builder,
        text="Add Hops",
        command=lambda: show_add_hops_window(
            window_root=window_root, hop_list=hop_list, hop_db=hop_db
        ),
    ).pack()
    Button(tab_recipe_builder, text="Save Recipe", command=save_recipe).pack()
