from app.schemas.user import Registration
from app.core.security import hash_password,verify_password

def register_user(registration : Registration):
    register_mail = registration.email
    register_pass = registration.password

    password_hash = hash_password(register_pass)
    return password_hash