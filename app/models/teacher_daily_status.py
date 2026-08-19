from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Uuid, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class TeacherDailyStatus(Base):
    __tablename__ = "teacher_daily_status"

    __table_args__ = (
        UniqueConstraint(
            "teacher_id",
            "status_date",
            name="uq_teacher_daily_status",
        ),
    )

    teacher_daily_status_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("teachers.teacher_id"),
        nullable=False,
    )

    status_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    teacher: Mapped["Teacher"] = relationship(
        back_populates="daily_status",
    )