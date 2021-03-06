from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import sqlite3
import datetime
import dbComms as db
import sys 

CONDITIONS = [
"Factory New",
"Minimal Wear",
"Field-Tested",
"Well-Worn",
"Battle Scarred"
] #Prepare quality conditions

home = Tk() #Home is an instance of Tk
home.title("Inventory Management Tool Version 0.1Alpha") #Set title

dateRaw = datetime.datetime.now()
dateNow = dateRaw.strftime("%Y-%m-%d %H:%M") #get the date in dateNow

# Create the database & it's table 
conn, c = db.initDB()
#db.makeTable("items")
db.initDB()

homeTabs = ttk.Notebook(home) #add tabs to home
checkTab = ttk.Frame(homeTabs) #add tab for checking in and out items
itemTab = ttk.Frame(homeTabs) #add tabs foor mannaging inventory

homeTabs.add(checkTab, text='Transactions') #add a tab
homeTabs.add(itemTab, text='Inventory') #add a tab
homeTabs.pack(expand=1, fill='both')

menu = Menu(home) #put a menu on home
dropdownExit = Menu(menu) #add a exit button
dropdownExit.add_command(label='Exit', command=exit)
menu.add_cascade(label='File', menu=dropdownExit) #order exit under file
home.config(menu=menu)

welcomeText = Label(checkTab, text="Select Check in or Check out")
welcomeText.grid(column=3, row=1, padx=10, pady=10)

chkInButton = Button(checkTab, text="Check in an item", padx=5, pady=5) #buttons
chkInButton.grid(column=2, row=2)
chkOutButton = Button(checkTab, text="Check out an item", padx=5, pady=5)
chkOutButton.grid(column=4, row=2)

#tree
itemTree = ttk.Treeview(home)

itemTree["columns"]=("items","issuer","recepiant","memo","date")
itemTree.column("items", width=100 )
itemTree.column("issuer", width=100)
itemTree.column("recepiant", width=100)
itemTree.column("memo", width=100)
itemTree.column("date", width=100)
itemTree.heading("items", text="Items")
itemTree.heading("issuer", text="Issuer")
itemTree.heading("recepiant", text="Recepiant")
itemTree.heading("memo", text="Memo")
itemTree.heading("date", text="Date")

itemTree.insert("" , 0, text="REEE", values=("Example Item Name","Jeff","Jeff","No Memo","qty",dateNow))

#id2 = itemTree.insert("", 1, "dir2", text="Dir 2")
#itemTree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))

##alternatively:
#itemTree.insert("", 3, "dir3", text="Dir 3")
#itemTree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

itemTree.pack()


#Next Page
itemNameLbl = Label(itemTab, text="Item Name")
conditionLbl = Label(itemTab, text="Condition")
memoLbl = Label(itemTab, text="Memo")
setOfLbl = Label(itemTab, text="Qry of Items")
itemNameLbl.grid(column=1, row=2)
conditionLbl.grid(column=1, row=3)
memoLbl.grid(column=1, row=4)
setOfLbl.grid(column=1, row=5)

imputDropDown = StringVar(home)
imputDropDown.set(CONDITIONS[0]) # default value

itemNameTxt = Entry(itemTab,width=15) #Normal Text Box
conditionMenu = OptionMenu(home, imputDropDown, *CONDITIONS) #Dropdown box
memoTxt = Entry(itemTab,width=15) #Normal Text Box
setOfBox = Spinbox(itemTab, from_=0, to=10,width=15)
itemNameTxt.grid(column=2,row=2)
conditionMenu.grid(column=2, row=3) #This needs to be fixed!!!!!
memoTxt.grid(column=2,row=4)
setOfBox.grid(column=2,row=5)
conditionMenu.pack()

def newItem():	#run if the new item button is clicked
	newItemList =[(itemNameTxt.get(), imputDropDown.get(), memoTxt.get(), setOfBox.get(), dateNow, 'nobody', 'nobody', 'in')]
	
	#insert data
	c.executemany('INSERT INTO items VALUES (?,?,?,?,?,?,?,?)', newItemList)
	print ("Added new item with data: ")
	print (newItemList)
	updateLists()

def updateLists():
	c.execute('SELECT * FROM items') #Select everything
	print(c.fetchall())
	
def exit():
	conn.commit() #commit database changes
	print("Init to Comit it")
	conn.close()
	sys.exit()

setNewItem = Button(itemTab, text="Add Item", command=newItem)
setNewItem.grid(column=2, row=1)

home.mainloop()
#conn.close() #close connection