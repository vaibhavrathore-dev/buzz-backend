
import smtplib
from email.message import EmailMessage
from app.models.user import User
from app.schemas.user import Send_Otp,Verifyotp
from app.core.config import settings
from app.core.security import generate_otp,hashed_otp,verify_otp
from app.models.otp_verification import Otpverification
from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import insert,select
from datetime import datetime, timedelta, timezone



def send_otp(recipient : Send_Otp,otp:str):
    message = EmailMessage()

    message["From"] = "buzzverfication@gmail.com"
    message["To"] = recipient.email
    message["Subject"] = "Otp for Email Verfication."
    message.set_content(
        f"Your Otp for Buzz Verification is {otp}.\n\n"
        f"This Otp Valid for only 5 minutes."
        )

    with smtplib.SMTP(settings.smtp_host,settings.smtp_port) as server:
        server.starttls()

        server.login(
            settings.smtp_username,
            settings.smtp_password
        )

        server.send_message(message)


    