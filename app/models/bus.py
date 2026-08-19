from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Bus(Base):
    __tablename__ = "buses"

    bus_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    bus_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    from_location: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    to_location: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    where_reached: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    where_parked: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )