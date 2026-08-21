from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.semester import Semester


class Course(Base):
    __tablename__ = "courses"

    course_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    department_id: Mapped[UUID] = mapped_column(ForeignKey("departments.department_id"), nullable=False)
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    department: Mapped["Department"] = relationship(back_populates="courses")
    semesters: Mapped[list["Semester"]] = relationship(back_populates="course")
