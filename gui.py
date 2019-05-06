from tkinter import *
from tkinter import ttk

home = Tk() #Home is an instance of Tk
home.title("Inventory Management Tool Version 0.1Alpha") #Set title

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
welcomeText.grid(column=3, row=1)

chkInButton = Button(checkTab, text="Check in an item")
chkInButton.grid(column=2, row=2)

chkOutButton = Button(checkTab, text="Check out an item")
chkOutButton.grid(column=4, row=2)

home.mainloop()