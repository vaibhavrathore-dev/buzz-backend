from getpass import getpass

from app.integrations.ums.client import UMSClient
from app.integrations.ums.parser import parse_dashboard


roll = input("University Roll Number: ")
password = getpass("UMS Password: ")

ums = UMSClient()

try:
    if not ums.login(roll, password):
        print("Login failed")
    else:
        dashboard = ums.get_dashboard()

        data = parse_dashboard(dashboard)

        print(data)

finally:
    ums.close()