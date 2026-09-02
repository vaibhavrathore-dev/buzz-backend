
from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, String, Uuid, ForeignKey,func,Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models import user

class refresh_token(Base):
    __tablename__ = "refresh_token"

    refresh_token_id : Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        nullable=False,
        server_default=func.gen_random_uuid()

    )

    user_id : Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey=("users.user_id"),
        nullable= False
    )

    token_hash : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False
    )

    expires_at : Mapped[datetime] = mapped_column(
         DateTime(timezone=True),
         nullable=False,
    )