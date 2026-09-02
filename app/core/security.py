from passlib.context import CryptContext
from app.core.config import settings
import secrets
from datetime import datetime,timezone,timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated=["auto"])

with open(settings.jwt_private_key,"r") as file:
    JWT_PRIVATE =  file.read()
with open(settings.jwt_public_key,"r") as file:
    JWT_PUBLIC = file.read()

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

def create_access_token(user_id,role):
    now = datetime.now(timezone.utc)
    payload = {
        "sub" : str(user_id),
        "role" : role,
        "iat" : now,
        "exp" : now + timedelta(minutes=15),
        "type" : "access"
        }
    token =  jwt.encode(payload,
                        JWT_PRIVATE,
                        algorithm="RS256")
    return token

def decode_access_token(token):
    payload = jwt.decode(
        token,
        JWT_PUBLIC,
        algorithms="RS256"
    )
    return payload

def create_refresh_token(user_id,role):
    now = datetime.now(timezone.utc)
    payload = {
        "sub" : str(user_id),
        "role" : role,
        "iat" : now,
        "exp" : now + timedelta(days =30),
        "type" : "refresh" 
    }
    token = jwt.encode(
        payload,
        JWT_PRIVATE,
        algorithm="RS256"
    )
    return token