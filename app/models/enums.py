from enum import Enum


class UserRole(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"


class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"


class DocumentType(str, Enum):
    PDF = "pdf"
    PPT = "ppt"
    PPTX = "pptx"
    DOC = "doc"
    DOCX = "docx"
    IMAGE = "image"
    OTHER = "other"