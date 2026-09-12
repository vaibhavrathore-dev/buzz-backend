
def parse_subjects(soup):
    subjects =[]
    attendance_link = soup.find_all(
        "a", string="Attendance"
    )
    
    for attendance in attendance_link:
        row = attendance.find_parent("tr")
        cells = row.find_all("td")
        subject_name = cells[0].get_text(" ",strip=True)
        assignments_link = row.find(
           "a" , string="Assignments"
        )
        attendance_url = attendance.get("href")
        assignments_url = assignments_link.get("href")
        subject = {
           "name" : subject_name,
           "assignment_url" : assignments_url,
           "attendance_url" : attendance_url
        }
        subjects.append(subject)
    return subjects
