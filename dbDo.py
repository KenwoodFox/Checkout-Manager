import sqlite3
import sys
import os
from os.path import isfile, getsize


def initDB(fileInQuestion): #database initDB
	print("looking for " + fileInQuestion  + ".db") #print to console
	if os.path.isfile(fileInQuestion + ".db"): #ask if the file exists
		print("Found File") #it exists

		conn = sqlite3.connect(fileInQuestion + '.db') #THIS DOES NOT WORK
		c = conn.cursor()
		return conn, c
	else: #it does not exist
	
		conn = sqlite3.connect(fileInQuestion + '.db') #THIS DOES NOT WORK
		c = conn.cursor()
		print("Did not find database, making new...") #alert console
		c.execute('''CREATE TABLE itemLoggedIn (itemName text, condition text, Memo text, setOf real, date text, issuer text, user text)''') #create a table for items in
		c.execute('''CREATE TABLE itemLoggedOut (itemName text, condition text, Memo text, setOf real, date text, issuer text, user text)''') #create a table for items out
	return conn, c

def addItem(content):
	c.executemany('INSERT INTO itemLoggedIn VALUES (?,?,?,?,?,?,?)', content) #insert content list into in
	conn.commit() #commit the change to the database

def deleteItem(content):
	#receive an item name
	#remove the line
	conn.commit() #commit the change to the database
	
def queryAll(table):
	c.execute('SELECT * FROM table') #Select everything
	print(c.fetchall())
	
def query(content):
	print("nothing")
	#receive a list
	#select all matching entries
	#return a much larger list