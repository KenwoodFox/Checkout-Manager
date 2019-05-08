import dbDo as dbDo
from tkinter import *
from tkinter import ttk

def loadNewFile(manifest):
    print("Loading New File")
    dbDo.initDB(manifest)


#dbDo.addItem([("Screwdriver", "Good", "No Memo", 4, "today", "Jeff", "Jhon")], "manifest")
