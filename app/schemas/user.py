from pydantic import BaseModel,EmailStr,field_validator
from app.models.enums import UserRole



class Registration(BaseModel):
    email : str
    password : str
    role : UserRole
    @field_validator("role")
    @classmethod
    def validate_role(cls, role):
        if role == UserRole.ADMIN:
            raise ValueError("Admin registration is not allowed")
        return role

class Send_Otp(BaseModel):
    email : EmailStr

class Verifyotp(BaseModel):
    email : EmailStr
    otp : str

class Login(BaseModel):
    email : EmailStr
    password : str

class Refresh_Token_Request(BaseModel):
    refresh_token : str

class ResetPassword(BaseModel):
    email: EmailStr
    otp: str
    new_password: str
    confirm_password: str