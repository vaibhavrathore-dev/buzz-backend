from bs4 import BeautifulSoup


def parse_dashboard(soup: BeautifulSoup):

    welcome = soup.find("h2")

    if welcome is None:
        raise RuntimeError("Student name not found")

    name = welcome.get_text(" ", strip=True)
    name = name.removeprefix("Welcome,").removesuffix("👋").strip()


    student_info = welcome.find_next("div")

    if student_info is None:
        raise RuntimeError("Student academic information not found")

    info = student_info.get_text(" ", strip=True)

    parts = [part.strip() for part in info.split("·")]

    if len(parts) != 4:
        raise RuntimeError("Unexpected student information format")

    course = parts[0]

    semester = int(
        parts[1].removeprefix("Sem").strip()
    )

    section = parts[2].removeprefix("Section").strip()

    roll = parts[3].removeprefix("Roll").strip()


    table = soup.find("table", class_="tb")

    if table is None:
        raise RuntimeError("Subjects table not found")

    tbody = table.find("tbody")

    if tbody is None:
        raise RuntimeError("Subjects table body not found")

    subjects = []

    for row in tbody.find_all("tr"):

        cells = row.find_all("td")

        if len(cells) < 5:
            continue

        subject_cell = cells[0]

        code_element = subject_cell.find("strong")

        if code_element is None:
            continue

        subject_code = code_element.get_text(strip=True)

        full_subject_text = subject_cell.get_text(
            " ",
            strip=True
        )

        class_info = subject_cell.find("div")

        class_text = (
            class_info.get_text(" ", strip=True)
            if class_info
            else ""
        )

        subject_name = full_subject_text

        subject_name = subject_name.replace(
            subject_code,
            "",
            1
        )

        if class_text:
            subject_name = subject_name.replace(
                class_text,
                "",
                1
            )

        subject_name = subject_name.lstrip("— ").strip()

        subject_type = cells[1].get_text(" ", strip=True)
        faculty_name = cells[2].get_text(" ", strip=True)

        phone_link = cells[3].find("a")
        email_link = cells[4].find("a")

        faculty_phone = (
            phone_link.get_text(strip=True)
            if phone_link
            else None
        )

        faculty_email = (
            email_link.get_text(strip=True)
            if email_link
            else None
        )

        subjects.append({
            "code": subject_code,
            "name": subject_name,
            "type": subject_type,
            "faculty": {
                "name": faculty_name,
                "phone": faculty_phone,
                "email": faculty_email,
            }
        })


    return {
        "student": {
            "name": name,
            "roll": roll,
            "course": course,
            "semester": semester,
            "section": section,
        },
        "subjects": subjects,
    }