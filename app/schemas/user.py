from pydantic import BaseModel,EmailStr

class Registration(BaseModel):
    email : str
    password : str

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