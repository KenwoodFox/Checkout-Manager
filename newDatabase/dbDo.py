import sqlite3
import sys
import os
from os.path import isfile, getsize

c = conn.cursor()

def initDB(fileInQuestion): #database initDB
	print("looking for " + fileInQuestion  + ".db") #print to console
	if os.path.isfile(fileInQuestion + ".db"): #ask if the file exists
		print("Found File") #it exists
		conn = sqlite3.connect(fileInQuestion + '.db') #connect to the database
	else: #it does not exist
		print("Did not find database, making new...") #alert console
		c.execute('''CREATE TABLE in (itemName text, condition text, Memo text, setOf real, date text, issuer text, user text)''') #create a table for items in
		c.execute('''CREATE TABLE out (itemName text, condition text, Memo text, setOf real, date text, issuer text, user text)''') #create a table for items out

def addItem(content)
	#recive a list
	#write the list
	conn.commit() #commit the change to the database

def deleteItem(content)
	#receive an item name
	#remove the line
	conn.commit() conn.commit() #commit the change to the database
	
def query(content)
	#receive a list
	#select all matching entries
	#return a much larger list