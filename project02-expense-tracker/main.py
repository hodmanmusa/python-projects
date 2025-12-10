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

        if selection == 3: 
            type = search_menu()
            print("Selection: ", type)
            if validate_search_input(type) is not False: 
                key = input(f"Enter key: ")
                search_records(key, type)
                log_operation("Success", f"Search {type} by key:{key}")
        
        if selection == 4: 
            display_expenses()
            record_no = input("Enter the record number to edit: ")
            display_single_expense(int(record_no))
            data = edit_record()
            update_record(record_no, data)

# ----------------------- Menu ----------------------
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

# ------------------- Add Expense ----------------
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

def load_data(): 
    with open("expense_tracker.json", "r") as file: 
        data = json.load(file)
    return data 

def display_expenses(data = load_data()):
    for index, d in enumerate(data,start=1): 
        print(f"\nRecord No: {index}")
        print(f'\tAmount: {d["amount"]}')
        print(f'\tDate: {d["date"]}')
        print(f'\tCategory: {d["category"]}')
        print(f'\tDescription: {d["description"]}')
        print("----------------------")
    print()

# ------- Search ---------------
def search_menu(): 
    print("Search expenses: ")
    print("You can search by the following keys: ")
    options = ["category", "date", "amount", "Amount Range"]

    for i, opt in enumerate(options, start=1): 
        print(f"{i}. Search by {opt}")
    selection = input("Enter your selection: ")
    return selection

def validate_search_input(selection): 
    try: 
        if not selection.isdigit(): 
            raise ValueError("The amount should be number.")
        if int(selection) not in range(1, 4): 
            raise Exception("The input is not in range. ")
    except ValueError as e: 
        print(e)
        return False 
    except Exception as e:
        print(e)
        return False 
    return selection


def search_records(key, selection): 
    data = load_data()
    selection = int(selection)
    
    filtered_data = []
    if selection == 1:
        filtered_data = [item for item in data if item.get('category')==key]
    elif selection == 2: 
        filtered_data = [item for item in data if item.get('date')==key]
    elif selection == 3: 
        filtered_data = [item for item in data if item.get('amount')==key]
    else: 
        print("Invalid Selection")
    
    if len(filtered_data)>0:
        display_expenses(filtered_data)
    else: 
        print("No data found for the specified key.") 
        log_operation("Error", "Search: No data found for the specified key")
        return 
    

# -------------------- Edit Expenses ----------------------------
def select_single_record(index_no: int): 
    data = load_data()
    record = data[index_no-1]
    return record

def display_single_expense(index_no:int):
    record = select_single_record(index_no)
    print(f"Category: {record['category']}")
    print(f"Amount: {record['amount']}")
    print(f"Date: {record['date']}")
    print(f"description: {record['description']}")
    

def edit_record(index_no:int): 
    # Display record that is going to be edited
    record = select_single_record(index_no)
    print(f"Category: {record['category']}")
    print(f"Amount: {record['amount']}")
    print(f"Date: {record['date']}")
    print(f"description: {record['description']}")
    
    # Edit the record
    print("Edit the record above by providing the following details: ")
    print("* If you don't want to edit a property just press enter: ")
    
    amount = input("Amount: ")
    if amount == '': 
        amount = record['amount']
    
    date = input("Date(YYYY-MM-DD): ")
    if date == '': 
        data=record['date']
    
    category = input("Category: ")
    if category == '': 
        category = record['category']

    description = input("Description: ")
    if description == '': 
        description = record['description']
    
    return (amount, date, category, description)

def update_record(record_no, data): 
    amount, date, category, description = data 
    record = select_single_record(record_no)
    
    edited_expense_dic = {'amount':amount, 'date':date, 'category':category, 'description':description}
    


# --------------------- Logging Operations -----------------------
def log_operation(status, operation):
    log_result = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "status":status, 
        "operation": operation, 
    }
    logger_config.log_operation(log_result)

if __name__ == "__main__": 
    start()