from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, Date, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.student import Student
    from app.models.subject_teacher import SubjectTeacher


class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    student_id: Mapped[UUID] = mapped_column(ForeignKey("students.student_id"), nullable=False)
    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"), nullable=False
    )
    attendance_date: Mapped[date] = mapped_column(Date, nullable=False)
    present: Mapped[bool] = mapped_column(Boolean, nullable=False)

    student: Mapped["Student"] = relationship(back_populates="attendance")
    subject_teacher: Mapped["SubjectTeacher"] = relationship(back_populates="attendance")
