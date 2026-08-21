from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, SmallInteger, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.section import Section
    from app.models.subject import Subject


class Semester(Base):
    __tablename__ = "semesters"
    __table_args__ = (
        UniqueConstraint("course_id", "semester_number", name="uq_course_semester"),
        CheckConstraint("semester_number >= 1 AND semester_number <= 12", name="ck_semester_number"),
    )

    semester_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    course_id: Mapped[UUID] = mapped_column(ForeignKey("courses.course_id"), nullable=False)
    semester_number: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    course: Mapped["Course"] = relationship(back_populates="semesters")
    sections: Mapped[list["Section"]] = relationship(back_populates="semester")
    subjects: Mapped[list["Subject"]] = relationship(back_populates="semester")
