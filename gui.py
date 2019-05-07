from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

import sqlite3

import datetime
dateRaw = datetime.datetime.now()
dateNow = dateRaw.strftime("%Y-%m-%d %H:%M")

home = Tk() #Home is an instance of Tk
home.title("Inventory Management Tool Version 0.1Alpha") #Set title
conn = sqlite3.connect('database.db') #establish a connection with the database
c = conn.cursor() #create a cursor object
#c.execute('''CREATE TABLE items (itemName text, condition text, Memo text, setOf real, date text, issuer text, user text, location text)''')

homeTabs = ttk.Notebook(home) #add tabs to home
checkTab = ttk.Frame(homeTabs) #add tab for checking in and out items
itemTab = ttk.Frame(homeTabs) #add tabs foor mannaging inventory

homeTabs.add(checkTab, text='Transactions') #add a tab
homeTabs.add(itemTab, text='Inventory') #add a tab
homeTabs.pack(expand=1, fill='both')

menu = Menu(home) #put a menu on home
dropdownExit = Menu(menu) #add a exit button
dropdownExit.add_command(label='Exit')
menu.add_cascade(label='File', menu=dropdownExit) #order exit under file
home.config(menu=menu)

welcomeText = Label(checkTab, text="Select Check in or Check out")
welcomeText.grid(column=3, row=1, padx=10, pady=10)

chkInButton = Button(checkTab, text="Check in an item", padx=5, pady=5) #buttons
chkInButton.grid(column=2, row=2)
chkOutButton = Button(checkTab, text="Check out an item", padx=5, pady=5)
chkOutButton.grid(column=4, row=2)

itemsOutWindow = scrolledtext.ScrolledText(checkTab,width=25,height=40)
itemsOutWindow.grid(column=2, row=3)

#Next Page

itemNameLbl = Label(itemTab, text="Item Name")
conditionLbl = Label(itemTab, text="Condition")
memoLbl = Label(itemTab, text="Memo")
setOfLbl = Label(itemTab, text="Number")
itemNameLbl.grid(column=1, row=3)
conditionLbl.grid(column=3, row=3)
memoLbl.grid(column=5, row=3)
setOfLbl.grid(column=7, row=3)

itemNameTxt = Entry(itemTab,width=15)
conditionTxt = Entry(itemTab,width=15)
memoTxt = Entry(itemTab,width=15)
setOfTxt = Entry(itemTab,width=15)
itemNameTxt.grid(column=2,row=3)
conditionTxt.grid(column=4,row=3)
memoTxt.grid(column=6,row=3)
setOfTxt.grid(column=8,row=3)

def newItem():	#run if the new item button is clicked
	itemname = itemNameTxt.get()
	condition = conditionTxt.get()
	memo = memoTxt.get()
	setOf = setOfTxt.get()
	
	#insert data
	c.execute("INSERT INTO items VALUES (itemName, condition, Memo, setOf, dateNow, 'fixthis', 'fixthis', 'in')")

setNewItem = Button(itemTab, text="Add Item", command=newItem)
setNewItem.grid(column=2, row=1)

home.mainloop()
conn.close() #close connection