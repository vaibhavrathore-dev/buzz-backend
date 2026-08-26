from fastapi import FastAPI , Depends , HTTPException
from app.schemas.user import Registration,Send_Otp
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.services.auth_service import registering_user
from app.services.email_service import send_otp,store_otp
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
def sending_otp(send : Send_Otp,
             db : Session = Depends(get_db)):
    result = db.execute(select(User).where(User.email == send.email))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    else:
        otp = store_otp(user,db)
        send_otp(send,otp)
        return " Email Sent Successfully"


