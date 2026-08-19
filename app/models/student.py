from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.user_id"),
        unique=True,
        nullable=False,
    )

    section_id: Mapped[UUID] = mapped_column(
        ForeignKey("sections.section_id"),
        nullable=False,
    )

    roll_number: Mapped[str] = mapped_column(
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
        back_populates="student",
    )

    section: Mapped["Section"] = relationship(
        back_populates="students",
    )

    attendance: Mapped[list["Attendance"]] = relationship(
        back_populates="student",
    )