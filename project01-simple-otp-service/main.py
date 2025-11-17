import utils
import logger
import time 
from datetime import datetime


def otp_verification (): 
    while True: 
        otp, created_at = utils.generate_otp()
        ttl = 30
        resend_requested = False

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
            
            if not is_input_valid(user_input): 
                print(f"Attempts {attempts}")
                log_result("Input Invalid", otp, attempts)
                continue

            if is_otp_expired(created_at, ttl): 
                print("The OTP time expired and is invalid.")
                print("Request a new one. ")
                log_result("Expired", otp, attempts)
                break 
            
            elif attempts==0: 
                print("OTP expired. No more attempts remeaning")
                break
            
            elif is_correct(otp, user_input): 
                print("Success. OTP validated!")
                log_result("Success", otp, attempts)
                break 

            else: 
                print("Error: Provide the OTP sent.")
                log_result("Failed", otp, attempts)

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
        int(user_otp)
        if len(user_otp)!=6: 
            raise Exception("The input length should be 6 digits.")
    
    except ValueError as e: 
        print("Value Erro: The input should be of type integer.", end=" ")
        return False
    
    except Exception as e: 
        print(e, end=" ")
        return False
    
    return True

def is_otp_expired(creatd_at, ttl): 
    elapsed = time.time() - creatd_at

    if elapsed>ttl: 
        return True 
    return False 



def is_correct(otp, user_otp):
    if otp == user_otp: 
        return True
    return False

def log_result(status, otp, attempts): 
    masked_otp = "".join(["*"]*4 + list(otp[-2:]))
    attempts_used = 3-attempts
    record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "otp": masked_otp, 
        "attempts":attempts_used, 
        "status":status
    }
    logger.log_session(record)


otp_verification()