from getpass import getpass
from app.integrations.agc.client import AGCClient

roll = input("University roll number: ")
password = getpass("AGC password: ")

agc = AGCClient()

result = agc.login(roll, password)

print("Login successful:", result)