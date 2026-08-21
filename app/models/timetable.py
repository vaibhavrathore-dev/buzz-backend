from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, Integer, SmallInteger, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.subject_teacher import SubjectTeacher
    from app.models.lecture_slot import LectureSlot


class Timetable(Base):
    __tablename__ = "timetable"
    __table_args__ = (
        CheckConstraint("day_of_week >= 1 AND day_of_week <= 6", name="ck_timetable_day"),
    )

    timetable_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"), nullable=False
    )
    lecture_slot_id: Mapped[int] = mapped_column(
        SmallInteger, ForeignKey("lecture_slots.lecture_slot_id"), nullable=False
    )
    day_of_week: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    subject_teacher: Mapped["SubjectTeacher"] = relationship(back_populates="timetables")
    lecture_slot: Mapped["LectureSlot"] = relationship(back_populates="timetables")
