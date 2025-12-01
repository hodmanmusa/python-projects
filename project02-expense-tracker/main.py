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

        selection = int(selection)
        
        if selection == 1: 
            expense = add_expense()
            if validate_expense(expense): 
                save_expense(expense)
                log_operation("Success", "New Expense")
        
        if selection == 2: 
            print("Displaying all expense records")
            display_expenses()
            log_operation("Success", "View All Expenses")

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
    date = input("Date(YYYY-MM-DD): ")
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
    try:
        with open("expense_tracker.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(expense_dict)

    with open("expense_tracker.json", "w") as f:
        json.dump(data, f, indent=4)

def display_expenses():
    with open("expense_tracker.json", "r") as file: 
        data = json.load(file)
    
    for index, d in enumerate(data,start=1): 
        print(f"\nRecord No: {index}")
        print(f'\tAmount: {d["amount"]}')
        print(f'\tDate: {d["date"]}')
        print(f'\tCategory: {d["category"]}')
        print(f'\tDescription: {d["description"]}')
        print("----------------------")
    print()
def log_operation(status, operation):
    log_result = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "status":status, 
        "operation": operation, 
    }
    logger_config.log_operation(log_result)

if __name__ == "__main__": 
    start()