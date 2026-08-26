from pydantic import BaseModel,EmailStr

class Registration(BaseModel):
    email : str
    password : str

class Send_Otp(BaseModel):
    email : EmailStr

class Verify_otp(BaseModel):
    email : EmailStr
    otp : str
