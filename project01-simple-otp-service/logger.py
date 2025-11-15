import json 

def log_session(record: dict): 
    with open("opt_log.txt", "a") as file: 
        file.write(json.dumps(record)+"\n")