from __future__ import annotations
from datetime import time
from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger, Time , CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.timetable import Timetable
    from app.models.assignment import Assignment


class LectureSlot(Base):
    __tablename__ = "lecture_slots"
    __table_args__ = (
        CheckConstraint(
            "start_time < end_time",
            name = "ck_lecture_slot_time"
        ),
    )

    lecture_slot_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)

    timetables: Mapped[list["Timetable"]] = relationship(back_populates="lecture_slot")
    assignments: Mapped[list["Assignment"]] = relationship(back_populates="lecture_slot")
