#
# dbComms.py
#
import sqlite3
from os.path import isfile, getsize

# Make a database, or if one exists, don't. 
def initDB():
    if isDB("manifest.db") == True:
        # db exists
        return
    else:
        conn = sqlite3.connect('manifest.db')
    c = conn.cursor()
    return conn, c

# is this the DB?
def isDB(filename):
    if not isfile(filename):
        return False
    if getsize(filename) < 100: #SQLite header is 100bytes
        return False
    
    with open(filename, 'rb') as fd:
        Header = fd.read(100)
    
    return Header[0:16] == b'SQLite format 3/000'

def makeTable(table):
    conn, c = initDB()
    
    c.execute('''CREATE TABLE items (itemName text, condition text, Memo text, setOf real, date text, issuer text, user text, location text)''')
    