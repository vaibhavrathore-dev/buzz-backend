from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"),
        nullable=False,
    )

    teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("teachers.teacher_id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    deadline: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    subject_teacher: Mapped["SubjectTeacher"] = relationship(
        back_populates="assignments",
    )

    teacher: Mapped["Teacher"] = relationship(
        back_populates="assignments",
    )