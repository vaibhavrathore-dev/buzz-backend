from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.subject_teacher import SubjectTeacher
    from app.models.teacher import Teacher


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"), nullable=False
    )
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teachers.teacher_id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    deadline: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    attachment_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()", nullable=False)

    subject_teacher: Mapped["SubjectTeacher"] = relationship(back_populates="assignments")
    teacher: Mapped["Teacher"] = relationship(back_populates="assignments")
