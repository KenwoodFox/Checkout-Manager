# encoding: utf8
import sys
import os

from tinydb import TinyDB, Query
checkedIn = TinyDB('checkedIn.json')
checkedOut = TinyDB('checkedOut.json')

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import pygubu


currentUser = "";

class Cribware:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()   #1: Create a builder
        builder.add_from_file('gui.ui') #2: Load an ui file
        self.mainwindow = builder.get_object('parentWidget', master)    #3: Create the widget using a master as parent
        #inventoryTree = builder.get_object('fullTree')
        builder.connect_callbacks(self)

        callbacks = {
            'login': self.login,
            'checkOut': self.checkOut,
            'checkIn': self.checkIn,
            'newItem': self.newItem,
            'removeItem': self.removeItem
            }

        builder.connect_callbacks(callbacks)

    def login(self):
        #messagebox.showinfo('Debug', self.builder.tkvariables['loginEntry'].get())
        currentUser = self.builder.tkvariables['loginEntry'].get()

    def checkIn(self):
        checkedIn.insert({'item': self.builder.tkvariables['checkInSelection'].get(),'returnUser': self.builder.tkvariables['returningUser'].get(),'memo':self.builder.tkvariables['checkInMemo'].get()})

        #debug = [self.builder.tkvariables['checkInSelection'].get(), self.builder.tkvariables['returningUser'].get(),self.builder.tkvariables['checkInMemo'].get()]
        #messagebox.showinfo('Debug', debug)

    def checkOut(self):
        checkedOut.insert({'item': self.builder.tkvariables['checkOutSelection'].get(),'issuedUser': self.builder.tkvariables['issuedUser'].get(),'memo':self.builder.tkvariables['checkOutMemo'].get()})

        #debug = [self.builder.tkvariables['checkOutSelection'].get(), self.builder.tkvariables['issuedUser'].get(),self.builder.tkvariables['checkOutMemo'].get()]
        #messagebox.showinfo('Debug', debug)

    def newItem(self):
        checkedIn.insert({'itemName': self.builder.tkvariables['newItemName'].get(), 'condition':  self.builder.tkvariables['newItemCondition'].get(), 'newItemMemo' : self.builder.tkvariables['newItemMemo'].get(), 'qty' : self.builder.tkvariables['newItemNumber'].get()})
        #inventoryTree.insert('', 'end', 'widgets', text='Widget Tour')

    def removeItem(self):
        debug = [self.builder.tkvariables['removeItemSelection'].get(), self.builder.tkvariables['itemRemovalNumber'].get()]
        messagebox.showinfo('Debug', debug)


if __name__ == '__main__':
    root = tk.Tk()
    app = Cribware(root)
    root.title("Inventory Management Tool Version 0.1Alpha") #Set title
    root.mainloop()
