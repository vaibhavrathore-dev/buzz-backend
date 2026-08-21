from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.department import Department
    from app.models.semester import Semester
    from app.models.section import Section
    from app.models.attendance import Attendance


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.user_id"), unique=True, nullable=False)
    department_id: Mapped[UUID] = mapped_column(ForeignKey("departments.department_id"), nullable=False)
    semester_id: Mapped[UUID] = mapped_column(ForeignKey("semesters.semester_id"), nullable=False)
    section_id: Mapped[UUID] = mapped_column(ForeignKey("sections.section_id"), nullable=False)
    roll_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    user: Mapped["User"] = relationship(back_populates="student")
    department: Mapped["Department"] = relationship()
    semester: Mapped["Semester"] = relationship()
    section: Mapped["Section"] = relationship(back_populates="students")
    attendance: Mapped[list["Attendance"]] = relationship(back_populates="student")
