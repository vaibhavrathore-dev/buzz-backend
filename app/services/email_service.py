import smtplib
from email.message import EmailMessage

from sqlalchemy import select
from sqlalchemy.orm import Session

from datetime import datetime, timedelta, timezone

from app.models.user import User
from app.models.otp_verification import Otpverification
from app.schemas.user import Send_Otp
from app.core.config import settings
from app.core.security import generate_otp, hashed_otp


def send_otp(s: Send_Otp, db: Session):

    result = db.execute(
        select(User).where(User.email == s.email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        return False

    if user.is_verified is True:
        return "Already Verified"

    result = db.execute(
        select(Otpverification)
        .where(Otpverification.user_id == user.user_id)
        .order_by(Otpverification.created_at.desc())
        .limit(1)
    )

    found = result.scalar_one_or_none()

    if found is not None:

        cooldown = found.created_at + timedelta(seconds=60)

        if datetime.now(timezone.utc) < cooldown:
            return "Wait"

        db.delete(found)

    otp = generate_otp()

    otp_hash = hashed_otp(otp)

    new_otp = Otpverification(
        user_id=user.user_id,
        otp_hash=otp_hash,
        attempts=0,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=5)
    )

    db.add(new_otp)

    message = EmailMessage()

    message["From"] = settings.smtp_username
    message["To"] = s.email
    message["Subject"] = "OTP for Email Verification"

    message.set_content(
        f"Your OTP for Buzz verification is {otp}.\n\n"
        f"This OTP is valid for only 5 minutes."
    )

    try:

        
        with smtplib.SMTP(
            settings.smtp_host,
            settings.smtp_port
        ) as server:

            server.starttls()

            server.login(
                settings.smtp_username,
                settings.smtp_password
            )

            server.send_message(message)


        db.commit()

        return "OTP Sent, Check Your Email"

    except Exception:

        db.rollback()
        return "OTP Sending Failed"