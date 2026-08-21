from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.semester import Semester
    from app.models.subject_teacher import SubjectTeacher


class Subject(Base):
    __tablename__ = "subjects"

    subject_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    semester_id: Mapped[UUID] = mapped_column(ForeignKey("semesters.semester_id"), nullable=False)
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    semester: Mapped["Semester"] = relationship(back_populates="subjects")
    subject_teachers: Mapped[list["SubjectTeacher"]] = relationship(back_populates="subject")
