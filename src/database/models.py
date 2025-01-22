from datetime import date
from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql.sqltypes import Date

from src.database.db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    second_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    phone: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    date_of_birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    def __repr__(self) -> str:
        return (f"Contact(id={self.id}, first_name={self.first_name}, second_name={self.second_name}, "
                f"email={self.email}, phone={self.phone}, date_of_birth={self.date_of_birth})")
