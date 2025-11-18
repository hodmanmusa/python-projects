import logging
import json 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSE_PATH = os.path.join(BASE_DIR, "expenses.json")

def log_operation(record:dict): 
    with open(EXPENSE_PATH, "a") as file: 
        file.write(file.write(json.dumps(record)+"\n"))