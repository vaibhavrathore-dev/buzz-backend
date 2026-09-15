from __future__ import annotations

from datetime import datetime,date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, Boolean,ForeignKey, String, Text, Uuid,Date,func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.subject_teacher import SubjectTeacher
    from app.models.lecture_slot import LectureSlot


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True,server_default=func.gen_random_uuid())
    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"), nullable=False
    )
    scheduled_date : Mapped[date] =mapped_column(Date,nullable=False)
    external_assignment_url : Mapped[str | None] = mapped_column(String,nullable=True)
    lecture_slot_id : Mapped[int] = mapped_column(ForeignKey("lecture_slots.lecture_slot_id"),nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    attachment_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default = func.now(), nullable=False)
    access_code_required: Mapped[bool] = mapped_column(
    Boolean,
    nullable=False,
    default=False,
    server_default="false"
)
    subject_teacher: Mapped["SubjectTeacher"] = relationship(back_populates="assignments")
    lecture_slot : Mapped["LectureSlot"] = relationship(back_populates="assignments")
