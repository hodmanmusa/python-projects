import utils


def otp_verification (): 
    otp = utils.generate_otp()

    print("---- OTP Verification ----")
    print("\nAn OTP has been sent to your device")
    print(f"OTP sent: {otp}")

otp_verification()