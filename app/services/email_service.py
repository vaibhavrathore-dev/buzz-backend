
import smtplib
from email.message import EmailMessage
from app.models.user import User
from app.schemas.user import Send_Otp,Verify_otp
from app.core.config import settings
from app.core.security import generate_otp,hashed_otp,verify_otp
from app.models.otp_verification import Otpverification
from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import insert
from datetime import datetime, timedelta, timezone



def send_otp(recipient : Send_Otp,otp:str):
    message = EmailMessage()

    message["From"] = "buzzverfication@gmail.com"
    message["To"] = recipient.email
    message.set_content(
        f"Your Otp for Buzz Verification is {otp}\n\n"
        f"This Otp Valid for only 3 minutes"
        )

    with smtplib.SMTP(settings.smtp_host,settings.smtp_port) as server:
        server.starttls()

        server.login(
            settings.smtp_username,
            settings.smtp_password
        )

        server.send_message(message)

def store_otp(us : User,
              db:Session):
    
    otp = generate_otp()
    hash = hashed_otp(otp)
    expires_at = expires_at = datetime.now(timezone.utc) + timedelta(minutes=3)
    result = insert(Otpverification).values(
        user_id = us.user_id,
        otp_hash = hash,
        expires_at = expires_at
    )
    db.execute(result)
    db.commit()
    
    return otp
    
    