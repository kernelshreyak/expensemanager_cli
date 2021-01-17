'''
	Expense Manager

	This python program can manage your daily/monthly/yearly expenses from the command line
	It also has data analysis features to get insights on your expenses

	Author: Shreyak Chakraborty (C) 2019
	License: GNU GPL v3
'''
import sys
from expense_mgr import *
from expense_analysis import *

def mainmenu():
	
	print("\nMain Menu:")
	print("1. Add Expense")
	print("2. Edit Expense")
	print("3. Delete Expense")
	print("4. View Expenses")
	print("4. About")
	print("5. Exit")

	print("\n\n")

	choice = str(input("Enter choice: "))

	

	if choice == "1":
		menu_addexpense()
		mainmenu()
	elif choice == "2":
		print("Edit expense TODO")
	elif choice == "3":
		print("Choice 3 TODO")
	elif choice == "4":
		print("Choice 1 TODO")
	elif choice == "5":
		exit()
	else:
		print("Invalid choice!")
		mainmenu()
	



def menu_addexpense():
	print("Add Expense (enter 'Ctrl + C' to return to Main Menu):")
	name = input("Enter expense name: ")
	amount = input("Enter expense amount: ")

	expense_add(str(name),float(amount))


# Driver code
if __name__ == "__main__":

	print("--------------Expense Manager--------------")
	mainmenu()




