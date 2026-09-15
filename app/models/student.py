from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID
from datetime import datetime   

from sqlalchemy import ForeignKey, String, Uuid,func,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.section import Section
    from app.models.attendance import Attendance


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True,server_default=func.gen_random_uuid())
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.user_id"), unique=True, nullable=False)
    section_id: Mapped[UUID] = mapped_column(ForeignKey("sections.section_id"), nullable=False)
    roll_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    user: Mapped["User"] = relationship(back_populates="student")
    section: Mapped["Section"] = relationship(back_populates="students")
    attendance: Mapped[list["Attendance"]] = relationship(back_populates="student")
    lab_group: Mapped[str | None] = mapped_column(
    String(50),
    nullable=True
)
    last_lms_sync_at: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True),
    nullable=True
)