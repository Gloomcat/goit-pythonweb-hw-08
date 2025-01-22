from typing import Optional

from datetime import date

from pydantic import BaseModel, Field, EmailStr, PastDate


class ContactModel(BaseModel):
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[PastDate] = Field(None, ge=date(1900, 1, 1))


class ContactCreateModel(ContactModel):
    first_name: str
    phone: str


class ContactResponseModel(ContactCreateModel):
    id: int
