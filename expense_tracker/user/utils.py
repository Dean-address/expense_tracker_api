import pyotp


def generate_otp():
    secret_key = pyotp.random_base32()
    otp = pyotp.TOTP(secret_key, interval=60)
    return otp.now()
