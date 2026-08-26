from app.schemas.user import Registration
from app.core.security import hash_password,verify_password,generate_otp
import smtplib


def registering_user(registration : Registration):
    email = registration.email
    password = registration.password

    password_hash = hash_password(password)
    return password_hash
