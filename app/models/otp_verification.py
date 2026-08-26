from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.student import Student
    from app.models.teacher import Teacher
    from app.models.notification import Notification

from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, String, Uuid, ForeignKey,func,Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Otpverification(Base):
    __tablename__ = "Otpverification"

    otp_id : Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
        nullable=False

    )

    user_id : Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("users.user_id"),
        nullable=False
    )
    otp_hash : Mapped[str] =  mapped_column(
        String(255),
        nullable=False
    )
    expires_at : Mapped[DateTime] = mapped_column(
         DateTime(timezone=True),
                server_default=func.now(),
                nullable=False
    )
    created_at : Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False

    )
