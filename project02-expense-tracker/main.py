import logger_config
import json
from datetime import datetime

def start():
    print("\n----------------------------")
    print("The Expense Tracker Program")
    print("")

    while True: 
        
        display_menu()
        selection = user_selection()
        
        if not is_selection_valid(selection): 
            break 
        
        if int(selection) == 1: 
            expense = add_expense()
            if validate_expense(expense): 
                save_expense(expense)

        

def display_menu(): 
    options = ['Add expense', 'View all expenses', 'Search expenses', 'Edit expense', 'Delete expense', 'Analysis & Aggregations', 'Undo last action', 'Exit']
    
    print("\nMenu options: ")
    print("------------------")

    for index, item in enumerate(options):
        print(f"{index+1}. {item}")

def user_selection(): 
    return input("Selection an option (1-8): ")

def is_selection_valid(selection): 
    try: 
        index = int(selection)
        if index not in range(1, 9): 
            raise Exception(f"The selected option is out of range.")
    except ValueError as e: 
        print("The input should be an integer")
        return False 
    except Exception as e: 
        print(e)
        return False 
    return True 

def add_expense(): 
    print("Add expense by providing the details below. ")
    amount = input("Amount: ")
    date = input("Date: ")
    category = input("Category: ")
    description = input("Description: ")
    return (amount, date, category, description)

def validate_expense(expense): 
    amount, date, *others = expense
    try: 
        if not amount.isdigit(): 
            raise ValueError("The amount should be number.")
        
        if not datetime.strptime(date, "%Y-%m-%d"): 
            raise TypeError("Date should be in format YYYY-MM-DD.") 
        
    except TypeError as te: 
        print(te)
        return False 
    except ValueError as ve: 
        print(ve)
        return False 
    except Exception as e:
        print(e)
    return True 

def save_expense(expense): 
    amount, date, category, description = expense
    expense_dict = {"amount": amount, "date": date,"category":category, "description":description}


if __name__ == "__main__": 
    start()