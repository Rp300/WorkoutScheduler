import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('user.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(name TEXT, major TEXT)')

def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES('2016-01-01', 'rish')")
	conn.commit()
	c.close()
	conn.close()


def dynamic_data_entry(name, classes):
	#unix = time.time()
	#date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = name
	#value = random.randrange(0,10)
	major = classes
	c.execute("INSERT INTO stuffToPlot (name, major) VALUES (?, ?)", 
		(keyword, major))
	conn.commit()

create_table()
#data_entry() 


for i in range(10):
	dynamic_data_entry("rohan", "chem")
	time.sleep(1)
c.close()
conn.close()