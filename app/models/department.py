from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.teacher_department import TeacherDepartment


class Department(Base):
    __tablename__ = "departments"

    department_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)

    courses: Mapped[list["Course"]] = relationship(back_populates="department")
    teacher_departments: Mapped[list["TeacherDepartment"]] = relationship(back_populates="department")
