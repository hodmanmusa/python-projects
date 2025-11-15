import utils


def otp_verification (): 
    otp = utils.generate_otp()

    print("---- OTP Verification ----")
    print("\nAn OTP has been sent to your device")
    print(f"OTP sent: {otp}")

    max_attempts = 3

    while max_attempts > 0: 
        max_attempts -= 1

        try: 
            input_otp = input("Enter OTP: ")
            int_input = int(input_otp)

        except ValueError as e: 
            print(f"Invalid input. Only numbers allowed.", end= " ")    
        
        if input_otp != otp and max_attempts>0: 
            print(f"Incorrect. Attempts left: {max_attempts}")
        elif input_otp == otp: 
            print("Verification successful.")
            return 
        else: 
            print("OTP expired. You reached the max attempts limit")


otp_verification()