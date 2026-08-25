from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated=["auto"])

def hash_password(password):
    hashed = pwd_context.hash(password)
    return hashed

def verify_password(password,hashed):
    is_correct = pwd_context.verify(password,hashed)
    return is_correct