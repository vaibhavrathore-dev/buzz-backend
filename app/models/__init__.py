from app.models.user import User
from app.models.department import Department
from app.models.course import Course
from app.models.semester import Semester
from app.models.section import Section
from app.models.subject import Subject
from app.models.teacher import Teacher
from app.models.student import Student
from app.models.teacher_department import TeacherDepartment
from app.models.subject_teacher import SubjectTeacher
from app.models.lecture_slot import LectureSlot
from app.models.timetable import Timetable
from app.models.attendance import Attendance
from app.models.assignment import Assignment
from app.models.notification import Notification
from app.models.bus import Bus
from app.models.teacher_daily_status import TeacherDailyStatus
from app.models.document import Document
from app.models.otp_verification import Otpverification
from app.models.refresh_tokens import RefreshToken

__all__ = [
    "User",
    "Department",
    "Course",
    "Semester",
    "Section",
    "Subject",
    "Teacher",
    "Student",
    "TeacherDepartment",
    "SubjectTeacher",
    "LectureSlot",
    "Timetable",
    "Attendance",
    "Assignment",
    "Notification",
    "Bus",
    "TeacherDailyStatus",
    "Document",
    "Otpverification",
    "RefreshToken"
]
