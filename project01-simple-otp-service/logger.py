import json 

def log_session(record: dict): 
    """
    Logs the session in JSON fromat to a file.

    Parameters
    ----------
    record: dict of session information 
    """

    with open("otp_log.txt", "a") as file: 
        file.write(json.dumps(record)+"\n")