from app.dependencies import get_current_user
from fastapi import Depends,HTTPException
from app.models.user import User

def verify_student(
        current_user : User = Depends(get_current_user)):
    if current_user.portal_verified:
        raise HTTPException(
            status_code=409,
            detail="Campus onboarding already completed"
        )
    return current_user 

    
    