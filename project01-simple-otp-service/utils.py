import random
import time

def generate_otp(length=6):
    """
    Return a random numeric OTP as a string.

    Parameters
    ----------
    length : int, optional
        Length of the OTP (default is 6).
    """

    digits = "0123456789"
    otp = ''.join([random.choice(digits) for x in range(length)])
    created_at = time.time()
    return (otp, created_at)
