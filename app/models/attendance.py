from datetime import date
from uuid import UUID

from sqlalchemy import Date, Enum, ForeignKey, Uuid, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import AttendanceStatus


class Attendance(Base):
    __tablename__ = "attendance"

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "subject_teacher_id",
            "attendance_date",
            name="uq_student_subject_attendance_date",
        ),
    )

    attendance_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.student_id"),
        nullable=False,
    )

    subject_teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("subject_teachers.subject_teacher_id"),
        nullable=False,
    )

    attendance_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[AttendanceStatus] = mapped_column(
        Enum(AttendanceStatus, name="attendance_status"),
        nullable=False,
    )

    student: Mapped["Student"] = relationship(
        back_populates="attendance",
    )

    subject_teacher: Mapped["SubjectTeacher"] = relationship(
        back_populates="attendance",
    )