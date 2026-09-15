from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid,UniqueConstraint,func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.semester import Semester
    from app.models.student import Student
    from app.models.subject_teacher import SubjectTeacher


class Section(Base):
    __tablename__ = "sections"
    __table_args__ = (
        UniqueConstraint(
            "semester_id",
            "name",
            name = "uq_semester_section"
        ),
    )

    section_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True , server_default=func.gen_random_uuid())
    semester_id: Mapped[UUID] = mapped_column(ForeignKey("semesters.semester_id"), nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    semester: Mapped["Semester"] = relationship(back_populates="sections")
    students: Mapped[list["Student"]] = relationship(back_populates="section")
    subject_teachers: Mapped[list["SubjectTeacher"]] = relationship(back_populates="section")
