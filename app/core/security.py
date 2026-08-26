from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated=["auto"])

def hash_password(password):
    hashed = pwd_context.hash(password)
    return hashed

def verify_password(password,hashed):
    is_correct = pwd_context.verify(password,hashed)
    return is_correct

def generate_otp():
    raw = secrets.randbelow(999999)
    otp = f"{raw:06d}"
    return otp

def hashed_otp(otp):
    hash_otp = pwd_context.hash(otp)
    return hash_otp

def verify_otp(hash_otp,otp):
    verify = pwd_context.verify(otp,hash_otp)
    return verify
