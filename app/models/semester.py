from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Semester(Base):
    __tablename__ = "semesters"

    semester_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    course_id: Mapped[UUID] = mapped_column(
        ForeignKey("courses.course_id"),
        nullable=False,
    )

    semester_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    course: Mapped["Course"] = relationship(
        back_populates="semesters",
    )

    sections: Mapped[list["Section"]] = relationship(
        back_populates="semester",
        cascade="all, delete-orphan",
    )

    subjects: Mapped[list["Subject"]] = relationship(
        back_populates="semester",
    )