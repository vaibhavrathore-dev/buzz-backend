from getpass import getpass

from app.integrations.ums.client import UMSClient


roll = input("University Roll Number: ")
password = getpass("UMS Password: ")

ums = UMSClient()

try:
    logged_in = ums.login(roll, password)

    print("Login successful:", logged_in)

    if logged_in:
        dashboard = ums.get_dashboard()
        with open("dashboard_debug.html", "w", encoding="utf-8") as file:
         file.write(str(dashboard))

        print("Dashboard fetched successfully")
        print("Page title:", dashboard.title.string if dashboard.title else "No title")

finally:
    ums.close()