import utils


def otp_verification (): 
    otp = utils.generate_otp()

    print("---- OTP Verification ----")
    print("\nAn OTP has been sent to your device")
    print(f"OTP sent: {otp}\n")

    input_validator(otp)


def input_validator(otp):
   
    max_attempts = 3

    while max_attempts > 0: 
        max_attempts -= 1
        
        try: 
            user_otp = input("Enter OTP: ")
            int(user_otp)
            if len(user_otp) != 6: 
                raise Exception(f"Invalid input: Please enter an integer of 6 digits. Attempts left: {max_attempts}")
        
        except ValueError as te: 
            print(f"Value Error: The input should be an Integer. Attempts left: {max_attempts}")

        except Exception as e: 
            print(e)
        
        if user_otp == otp: 
            print("Validated Successfuly. ")
            return 
        else: 
            print(f"The entered OTP is not correct. Please try again. Attempts left{max_attempts}")
        
        if max_attempts == 0: 
            code = input("To resend a new OTP type 'resend': ")
            if code.lower() == 'resend': 
                otp_verification()
            return 
            
otp_verification()