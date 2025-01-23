from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas import ContactCreateModel, ContactModel


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self, body: ContactCreateModel):
        return await self.repository.create_contact(body)

    async def seed_contacts(self, count: int):
        await self.repository.seed_contacts(count)

    async def get_contacts(
        self,
        skip: int | None = None,
        limit: int | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        birthdays: bool = False,
    ):
        return await self.repository.get_contacts(
            skip, limit, first_name, last_name, email, birthdays
        )

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)
