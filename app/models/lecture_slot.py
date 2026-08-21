from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.timetable import Timetable


class LectureSlot(Base):
    __tablename__ = "lecture_slots"

    lecture_slot_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    start_time: Mapped[object] = mapped_column(Time, nullable=False)
    end_time: Mapped[object] = mapped_column(Time, nullable=False)

    timetables: Mapped[list["Timetable"]] = relationship(back_populates="lecture_slot")
