from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    course_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.department_id"),
        nullable=False,
    )

    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    department: Mapped["Department"] = relationship(
        back_populates="courses",
    )

    semesters: Mapped[list["Semester"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan",
    )