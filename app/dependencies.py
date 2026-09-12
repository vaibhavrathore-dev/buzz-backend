from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials 
from app.models.user import User
from app.models.enums import UserRole
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
from app.core.security import decode_access_token
from sqlalchemy import select
from app.database import get_db
from jose import JWTError
security = HTTPBearer()
def get_current_user(
        credentials : HTTPAuthorizationCredentials = Depends(security),
        db : Session = Depends(get_db)
):
    token = credentials.credentials
    try:
        decode = decode_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    user_id = decode.get("sub")
    typ = decode.get("type")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token Payload"
        )
    if typ != "access":
        raise HTTPException(
            status_code=401,
            detail="Invalid token type"
        )
    result = db.execute(select(User).where(User.user_id == user_id))
    us = result.scalar_one_or_none()
    if us is None:
        raise HTTPException(
                status_code=401,
                detail="User not Found"
        )
    if us.is_active is False:
        raise HTTPException(
            status_code=401,
            detail="User's account Inactive",
        )
    if us.is_verified is False:
        raise HTTPException(
            status_code=401,
            detail="User not Verified"
        )
 
    return us

def require_teacher(current_user : User = Depends(get_current_user)):
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(
            status_code=403,
            detail="Teacher acess required"
        )
    return current_user

def require_student(current_user : User = Depends(get_current_user)):
    if current_user.role != UserRole.STUDENT:
        raise HTTPException(
            status_code=403,
            detail="Student acess required"
        )
    return current_user

def require_admin(current_user : User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=403,
            detail="Admin acess required"
        )
    return current_user