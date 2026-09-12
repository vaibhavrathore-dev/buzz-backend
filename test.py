from getpass import getpass

from app.integrations.agc.client import AGCClient
from app.integrations.agc.parsers.dashboard import parse_subjects

uni = input("Enter Your RollNo.: ")
password = getpass("Enter Your Portal Password: ")

agc = AGCClient()

if agc.login(uni, password):

    dashboard = agc.get_dashboard()

    subjects = parse_subjects(dashboard)

    for subject in subjects:
        print(subject)