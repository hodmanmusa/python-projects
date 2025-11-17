import utils
import logger
import time 
from datetime import datetime


def otp_verification (): 
    while True: 
        otp, created_at = utils.generate_otp()
        ttl = 30
        resend_requested = False
        attempts_used = 0
        status_message = ""

        print("---- OTP Verification ----")
        print("\nOTP has been sent to your device")
        print(f"Your OTP is: {otp}\n")

        print("\nPlease Enter the 6-digit OTP.")
        print("Type 'resend' to get a new code.")

        attempts = 3 

        while attempts > 0: 
            attempts-=1
            user_input = get_user_input()

            if wants_resend(user_input): 
                resend_requested = True 
                break
            attempts_used += 1
            
            if not is_input_valid(user_input): 
                print(f"Attempts {attempts}")
                status_message = "Invalid Input"
                continue


            if is_otp_expired(created_at, ttl): 
                print("The OTP time expired and is invalid.")
                print("Request a new one. ")
                status_message = "expired"
                break 
            
            elif attempts==0: 
                print("OTP expired. No more attempts remaining")
                status_message = "failed"
                break
            
            elif is_correct(otp, user_input): 
                print("Success. OTP validated!")
                status_message = "success"
                break 

            else: 
                print("Error: Provide the OTP sent.")
                status_message = "failed"

        print_session_info(status_message, otp, attempts_used)
        log_result(status_message, otp, attempts_used)
        if not resend_requested: 
            break

def wants_resend(user_input):
    if user_input.lower().strip() == 'resend': 
        return True
    return False 

def get_user_input(): 
    return input("\nEnter OTP or 'resend': ")

def is_input_valid(user_otp): 
    try: 
        if not user_otp.isdigit():
            raise ValueError("Value Error: The input should be of type integer.")
        if len(user_otp)!=6: 
            raise Exception("The input length should be 6 digits.")
    
    except ValueError as e: 
        print(e, end=" ")
        return False
    
    except Exception as e: 
        print(e, end=" ")
        return False
    
    return True

def is_otp_expired(creatd_at, ttl): 
    elapsed = time.time() - creatd_at
    return elapsed>ttl

def is_correct(otp, user_otp):
    if otp == user_otp: 
        return True
    return False

def print_session_info(message, otp, attempts_used):
    print("\nSession info: ")
    print("---------------------")
    print(f"OTP: {otp}")
    print(f"Status: {message}")
    print(f"Attempts: {attempts_used}")

def log_result(status, otp, attempts_used): 
    masked_otp = "".join(["*"]*4 + list(otp[-2:]))
    record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "otp": masked_otp, 
        "attempts":attempts_used, 
        "status":status
    }
    logger.log_session(record)



if __name__ == "__main__":
    otp_verification()