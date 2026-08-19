from uuid import UUID

from sqlalchemy import ForeignKey, Uuid, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class TeacherDepartment(Base):
    __tablename__ = "teacher_departments"

    __table_args__ = (
        UniqueConstraint(
            "teacher_id",
            "department_id",
            name="uq_teacher_department",
        ),
    )

    teacher_department_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    teacher_id: Mapped[UUID] = mapped_column(
        ForeignKey("teachers.teacher_id"),
        nullable=False,
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.department_id"),
        nullable=False,
    )

    teacher: Mapped["Teacher"] = relationship(
        back_populates="departments",
    )

    department: Mapped["Department"] = relationship(
        back_populates="teachers",
    )