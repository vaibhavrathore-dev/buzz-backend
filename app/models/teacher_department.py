from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.teacher import Teacher
    from app.models.department import Department


class TeacherDepartment(Base):
    __tablename__ = "teacher_departments"

    teacher_department_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teachers.teacher_id"), nullable=False)
    department_id: Mapped[UUID] = mapped_column(ForeignKey("departments.department_id"), nullable=False)

    teacher: Mapped["Teacher"] = relationship(back_populates="teacher_departments")
    department: Mapped["Department"] = relationship(back_populates="teacher_departments")
