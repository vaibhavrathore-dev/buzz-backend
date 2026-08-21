from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.teacher_department import TeacherDepartment
    from app.models.subject_teacher import SubjectTeacher
    from app.models.assignment import Assignment
    from app.models.document import Document
    from app.models.teacher_daily_status import TeacherDailyStatus


class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.user_id"), unique=True, nullable=False)
    employee_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    user: Mapped["User"] = relationship(back_populates="teacher")
    teacher_departments: Mapped[list["TeacherDepartment"]] = relationship(back_populates="teacher")
    subject_teachers: Mapped[list["SubjectTeacher"]] = relationship(back_populates="teacher")
    assignments: Mapped[list["Assignment"]] = relationship(back_populates="teacher")
    documents: Mapped[list["Document"]] = relationship(back_populates="teacher")
    daily_statuses: Mapped[list["TeacherDailyStatus"]] = relationship(back_populates="teacher")
