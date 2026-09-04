from fastapi import FastAPI , Depends , HTTPException
from app.schemas.user import Registration,Send_Otp,Verifyotp,Login,Refresh_Token_Request
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select,insert
from app.models.user import User
from app.models.otp_verification import Otpverification
from app.services.auth_service import registering_user,store_otp,verifying_otp,logging
from app.services.email_service import send_otp,forgot_otp
from app.core.security import decode_refresh,create_access_token
from app.models.refresh_tokens import RefreshToken
import hashlib
app = FastAPI()

@app.post("/register")
def register_user(register : Registration,
                  db : Session = Depends(get_db)):
    result = db.execute(
        select(User).where(User.email == register.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )
    if existing_user is None:
        hashed =registering_user(register)
        user =  User(email = register.email,password_hash = hashed)
        db.add(user)
        db.commit()
        db.refresh(user)
        return "Email Registered Successfully"

@app.post("/send_otp")
def sending_otp(
    s: Send_Otp,
    db: Session = Depends(get_db)
):
    result = send_otp(s, db)

    if result is False:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    if result == "Already Verified":
        raise HTTPException(
            status_code=400,
            detail="This email is already verified"
        )

    if result == "Wait":
        raise HTTPException(
            status_code=429,
            detail="Please wait before requesting another OTP"
        )

    if result == "OTP Sending Failed":
        raise HTTPException(
            status_code=500,
            detail="OTP Sending Failed"
        )

    return {"message": "Email Sent Successfully"}

@app.post("/verify_otp")
def verify_otp_route(
    ver: Verifyotp,
    db: Session = Depends(get_db)
):
    result = verifying_otp(ver, db)

    if result:
        return "Email Verified Successfully"

    raise HTTPException(
        status_code=400,
        detail="Invalid or Expired OTP"
    )

@app.post("/login")
def log_in(log : Login,db : Session = Depends(get_db)):
   result = logging(log, db)

   if result is False:
       raise HTTPException(
           status_code=401,
           detail = "Invalid email or password"
       )

   if result == "Inactive":
    raise HTTPException(
        status_code=403,
        detail="Account is inactive"
    )

   if result == "Unverified":
       raise HTTPException(
           status_code=403,
           detail="Account is Unverified"
       )

   return {
    "access_token": result["access_token"],
    "refresh_token": result["refresh_token"],
    "token_type": "bearer"
    }

@app.post("/refresh")
def refresh(r : Refresh_Token_Request,db : Session = Depends(get_db)):
    payload = decode_refresh(r.refresh_token)

    print("PAYLOAD:", payload)
    print("TOKEN TYPE:", payload.get("type"))
    if payload.get("type") == "refresh":
        user_id = payload.get("sub")
        role = payload.get("role")
        hashed = hashlib.sha3_256(
            r.refresh_token.encode()
            ).hexdigest()
        print("USER ID:", user_id)
        print("HASH FROM REQUEST:", hashed)

        to = db.execute(select(RefreshToken).where(RefreshToken.user_id == user_id,RefreshToken.token_hash == hashed))
        ken = to.scalar_one_or_none()

        print("DATABASE RESULT:", ken)
        if ken is None:
                    raise HTTPException(
                        status_code=403,
                        detail="Invalid refresh token"
                    )
        
        return create_access_token(user_id , role)
      

    else:
        raise HTTPException(
            status_code=403,
            detail="Invalid refresh token"
        )
            
@app.post("/logout")
def logout(r : Refresh_Token_Request,db : Session = Depends(get_db)):
    hashed = hashlib.sha3_256(
                r.refresh_token.encode()
                ).hexdigest()
    table = db.execute(select(RefreshToken).where(RefreshToken.token_hash == hashed))
    to = table.scalar_one_or_none()

    if to is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid refresh token or Already Logged out"
        )  
    db.delete(to)
    db.commit()
    return "Successfully Logged out"

@app.post("/forgot_password")
def sending_forgot_otp(
    s: Send_Otp,
    db: Session = Depends(get_db)
):
    result = forgot_otp(s, db)

    if result == "Wait":
        raise HTTPException(
            status_code=429,
            detail="Please wait before requesting another OTP"
        )

    if result == "OTP Sending Failed":
        raise HTTPException(
            status_code=500,
            detail="Unable to send OTP"
        )

    if result is False:
        return {
            "message": "If this email is eligible, an OTP has been sent"
        }

    return {
        "message": "OTP sent successfully"
    }