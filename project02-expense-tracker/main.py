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


if __name__ == "__main__": 
    start()