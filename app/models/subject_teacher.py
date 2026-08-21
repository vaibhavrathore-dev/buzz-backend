from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Uuid, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.teacher import Teacher
    from app.models.subject import Subject
    from app.models.section import Section
    from app.models.timetable import Timetable
    from app.models.attendance import Attendance
    from app.models.assignment import Assignment
    from app.models.document import Document


class SubjectTeacher(Base):
    __tablename__ = "subject_teachers"
    __table_args__ = (
        UniqueConstraint(
            "teacher_id", "subject_id", "section_id",
            name="uq_subject_teacher_section"
        ),
    )

    subject_teacher_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teachers.teacher_id"), nullable=False)
    subject_id: Mapped[UUID] = mapped_column(ForeignKey("subjects.subject_id"), nullable=False)
    section_id: Mapped[UUID] = mapped_column(ForeignKey("sections.section_id"), nullable=False)

    teacher: Mapped["Teacher"] = relationship(back_populates="subject_teachers")
    subject: Mapped["Subject"] = relationship(back_populates="subject_teachers")
    section: Mapped["Section"] = relationship(back_populates="subject_teachers")
    timetables: Mapped[list["Timetable"]] = relationship(back_populates="subject_teacher")
    attendance: Mapped[list["Attendance"]] = relationship(back_populates="subject_teacher")
    assignments: Mapped[list["Assignment"]] = relationship(back_populates="subject_teacher")
    documents: Mapped[list["Document"]] = relationship(back_populates="subject_teacher")
