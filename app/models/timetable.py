from uuid import UUID

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    SmallInteger,
    Uuid,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Timetable(Base):
    __tablename__ = "timetable"

    __table_args__ = (
        CheckConstraint(
            "day_of_week >= 1 AND day_of_week <= 6",
            name="check_timetable_day",
        ),
        UniqueConstraint(
            "subject_teacher_id",
            "lecture_slot_id",
            "day_of_week",
            name="uq_timetable_entry",
        ),
    )

    timetable_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"),
        nullable=False,
    )

    lecture_slot_id: Mapped[UUID] = mapped_column(
        ForeignKey("lecture_slots.lecture_slot_id"),
        nullable=False,
    )

    day_of_week: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
    )

    subject_teacher: Mapped["SubjectTeacher"] = relationship(
        back_populates="timetable",
    )

    lecture_slot: Mapped["LectureSlot"] = relationship(
        back_populates="timetable",
    )