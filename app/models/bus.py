from __future__ import annotations

from uuid import UUID

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Bus(Base):
    __tablename__ = "buses"

    bus_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    bus_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    from_location: Mapped[str] = mapped_column(String(150), nullable=False)
    to_location: Mapped[str] = mapped_column(String(150), nullable=False)
    where_reached: Mapped[str | None] = mapped_column(String(150), nullable=True)
    where_parked: Mapped[str | None] = mapped_column(String(150), nullable=True)
