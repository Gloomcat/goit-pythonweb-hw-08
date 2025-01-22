import re
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.database.db import get_db
from src.schemas import ContactCreateModel, ContactResponseModel, ContactModel
from src.services.contacts import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])


def extract_integrity_error_message(error: IntegrityError) -> str:
    error_str = str(error.orig)
    if "duplicate key value" in error_str:
        match = re.search(r"Key \((\w+)\)=\((.*?)\)", error_str)
        if match:
            column_name, value = match.groups()
            return f"The value '{value}' for '{column_name}' is already taken. Please use another one."

    return "A database integrity error occurred. Please check your input."


@router.get("/", response_model=List[ContactResponseModel])
async def read_contacts(
    skip: int = 0,
    limit: int = Query(default=10, le=100, ge=10),
    first_name: str | None = Query(default=None),
    last_name: str | None = Query(default=None),
    email: str | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
):
    contact_service = ContactService(db)
    contacts = await contact_service.get_contacts(
        skip, limit, first_name, last_name, email
    )
    return contacts


@router.get("/{contact_id}", response_model=ContactResponseModel)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.get_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.post(
    "/", response_model=ContactResponseModel, status_code=status.HTTP_201_CREATED
)
async def create_contact(body: ContactCreateModel, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    try:
        return await contact_service.create_contact(body)
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=extract_integrity_error_message(e),
        )


@router.put("/{contact_id}", response_model=ContactResponseModel)
async def update_contact(
    body: ContactModel, contact_id: int, db: AsyncSession = Depends(get_db)
):
    contact_service = ContactService(db)
    try:
        contact = await contact_service.update_contact(contact_id, body)
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=extract_integrity_error_message(e),
        )
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponseModel)
async def remove_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.remove_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact
