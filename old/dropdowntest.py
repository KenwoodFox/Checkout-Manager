from tkinter import *

CONDITIONS = [
"Factory New",
"Minimal Wear",
"Field-Tested",
"Well-Worn",
"Battle Scarred"
] #Prepare quality conditions

master = Tk()

variable = StringVar(master)
variable.set(CONDITIONS[0]) # default value

w = OptionMenu(master, variable, *CONDITIONS)
w.pack()

mainloop()