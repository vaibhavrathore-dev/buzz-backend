from datetime import time
from uuid import UUID

from sqlalchemy import Time, Uuid, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class LectureSlot(Base):
    __tablename__ = "lecture_slots"

    lecture_slot_id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    slot_number: Mapped[int] = mapped_column(
        nullable=False,
        unique=True,
    )

    start_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    end_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    timetable: Mapped[list["Timetable"]] = relationship(
        back_populates="lecture_slot",
    )