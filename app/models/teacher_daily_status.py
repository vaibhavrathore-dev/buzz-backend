from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, Date, ForeignKey, Text, Uuid, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.teacher import Teacher


class TeacherDailyStatus(Base):
    __tablename__ = "teacher_daily_status"
    __table_args__ = (
        UniqueConstraint("teacher_id", "status_date", name="uq_teacher_daily_status_date"),
    )

    teacher_daily_status_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teachers.teacher_id"), nullable=False)
    status_date: Mapped[date] = mapped_column(Date, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    note: Mapped[str | None] = mapped_column(Text, nullable=True)

    teacher: Mapped["Teacher"] = relationship(back_populates="daily_statuses")
