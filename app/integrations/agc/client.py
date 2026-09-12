import httpx
from bs4 import BeautifulSoup

class AGCClient:
    BASE_URL = "https://agclms.in"

    def __init__(self):
      self.client = httpx.Client(
        base_url=self.BASE_URL,
        follow_redirects=True,
        timeout=10.0
     )

    def get_login_token(self):
     response = self.client.get("/Elogin/StudentLogin")
     soup = BeautifulSoup(response.text,"html.parser")
     token_element =  soup.find("input" , {"name" : "__RequestVerificationToken"})
     if token_element is None:
            print("AGC verification token not found")
     else:
      value = token_element.get("value")
      return value
   
    def login(self,uni_roll_num : str , password : str):
        token = self.get_login_token()
        data = {
            "StudentId" : uni_roll_num,
            "Password" : password,
            "__RequestVerificationToken" : token
        }    
        response = self.client.post("/Elogin/StudentLogin",data=data)
        return response.url.path == "/DashBoardStudent"

    def get_dashboard(self):
     response = self.client.get("/DashBoardStudent")

     response.raise_for_status()

     if response.url.path != "/DashBoardStudent":
        raise RuntimeError("AGC session is not authenticated")

     soup = BeautifulSoup(response.text, "html.parser")

     return soup