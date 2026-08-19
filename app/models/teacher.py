from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.user_id"),
        unique=True,
        nullable=False,
    )

    employee_id: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        back_populates="teacher",
    )

    departments: Mapped[list["TeacherDepartment"]] = relationship(
        back_populates="teacher",
        cascade="all, delete-orphan",
    )

    subject_teachers: Mapped[list["SubjectTeacher"]] = relationship(
        back_populates="teacher",
    )

    assignments: Mapped[list["Assignment"]] = relationship(
        back_populates="teacher",
    )

    documents: Mapped[list["Document"]] = relationship(
        back_populates="uploaded_by",
    )

    daily_status: Mapped[list["TeacherDailyStatus"]] = relationship(
        back_populates="teacher",
    )