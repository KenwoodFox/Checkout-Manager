import dbDo as dbDo
from tkinter import *
from tkinter import ttk

dbDo.initDB("manifest")
print("Loading Gui")

def addItem(content, database):
	c.executemany('INSERT INTO itemLoggedIn VALUES (?,?,?,?,?,?,?)', content) #insert content list into in
	conn.commit() #commit the change to the database

#dbDo.addItem([("Screwdriver", "Good", "No Memo", 4, "today", "Jeff", "Jhon")], "manifest")
addItem([("Screwdriver", "Good", "No Memo", 4, "today", "Jeff", "Jhon")], "manifest")
