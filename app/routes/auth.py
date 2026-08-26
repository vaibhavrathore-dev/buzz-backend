from fastapi import FastAPI , Depends , HTTPException
from app.schemas.user import Registration
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.core.security import hash_password

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
        hashed = hash_password(register.password)
        user =  User(email = register.email,password_hash = hashed)
        db.add(user)
        db.commit()
        db.refresh(user)
        return "Email Registered Successfully"



