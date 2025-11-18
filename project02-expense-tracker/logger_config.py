import logging
import json 

def log_operation(record:dict): 
    with open("expense_logger.txt", "a") as file: 
        file.write(file.write(json.dumps(record)+"\n"))