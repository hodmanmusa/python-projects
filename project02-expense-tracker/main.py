import logger_config
import json
from datetime import datetime

def display_menu(): 
    options = ['Add expense', 'View all expenses', 'Search expenses', 'Edit expense', 'Delete expense', 'Analysis & Aggregations', 'Undo last action', 'Exit']
    
    print("Menu options: ")
    print("------------------")

    for index, item in enumerate(options):
        print(f"{index+1}. {item}")


if __name__ == "__main__": 
    display_menu()