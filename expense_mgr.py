'''
	Expense Manager

	This python program can manage your daily/monthly/yearly expenses from the command line
	It also has data analysis features to get insights on your expenses
	
	This can also be used as a standalone module for incoroporating expenses management features 
	in other Python application backends as well

	Author: Shreyak Chakraborty (C) 2019
	License: GNU GPL v3
'''

# This file contains the main functions and classes to perform CRUD operations of expense and related data

import sqlite3

def db_init():

	conn = sqlite3.connect('db.sqlite3')

	return conn,conn.cursor()

def expense_add(name,amount):
	conn,cursor = db_init() 

	cursor.execute("INSERT INTO expenses VALUES(1,?,?)",(name,amount))


