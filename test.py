from getpass import getpass

from app.integrations.agc.client import AGCClient
from app.integrations.agc.parsers.dashboard import parse_subjects

uni = input("Enter Your RollNo.: ")
password = getpass("Enter Your Portal Password: ")

agc = AGCClient()
if agc.login(uni, password):
    profile = agc.get_profile()
    for tag in profile.find_all(["div", "p", "h1", "h2", "h3", "h4", "span", "td"]):
     text = tag.get_text(" ", strip=True)

     if text and len(text) < 120:
        print(tag.name, "->", text)