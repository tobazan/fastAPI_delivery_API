import datetime
from typing import Optional
from pydantic import validator, EmailStr
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    username: str = Field(index=True, min_length=4)
    password: str = Field(max_length=256, min_length=8)
    email: EmailStr
    name: str = Field(min_length=4)
    phone: str = Field(min_length=4)
    is_admin: bool = False
    is_active: bool = True
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()


class UserInput(SQLModel):
    username: str
    password: str = Field(max_length=256, min_length=8)
    password2: str = Field(max_length=256, min_length=8)
    email: EmailStr
    name: str = Field(min_length=4)
    phone: str = Field(min_length=4)

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
    
class UserOutput(SQLModel):
    username: str
    email: EmailStr
    name: str
    phone: str
    is_admin: bool
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserLogin(SQLModel):
    username: str
    password: str