from app.schemas.user import Registration
from app.core.security import hash_password,verify_password,generate_otp
from app.models.otp_verification import Otpverification
from sqlalchemy.orm import Session
from sqlalchemy import insert,select
from datetime import datetime, timedelta, timezone
from app.models.user import User
from app.schemas.user import Send_Otp,Verifyotp
from app.core.security import generate_otp,hashed_otp,verify_otp



def registering_user(registration : Registration):
    email = registration.email
    password = registration.password

    password_hash = hash_password(password)
    return password_hash


def store_otp(us : User,
              db:Session):
    
    otp = generate_otp()
    hash = hashed_otp(otp)
    expires_at = expires_at = datetime.now(timezone.utc) + timedelta(minutes=5)
    result = insert(Otpverification).values(
        user_id = us.user_id,
        otp_hash = hash,
        expires_at = expires_at
    )
    db.execute(result)
    db.commit()
    
    return otp

def verifying_otp(verify : Verifyotp,
               db:Session):
     result = db.execute(select(User).where(User.email == verify.email))
     user = result.scalar_one_or_none()
     find = db.execute(
    select(Otpverification)
    .where(Otpverification.user_id == user.user_id)
    .order_by(Otpverification.created_at.desc())
    .limit(1)
)
     found = find.scalar_one_or_none()
     hash_otp = found.otp_hash
     
     expiry = found.expires_at

     if expiry > datetime.now(timezone.utc):
             verified = verify_otp(hash_otp,verify.otp)
             return verified
     else:
             return False
             
