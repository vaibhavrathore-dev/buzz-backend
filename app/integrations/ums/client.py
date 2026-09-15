import httpx
from bs4 import BeautifulSoup


class UMSClient:
   BASE_URL = "https://umsagc.in"

   def __init__(self):
      self.client = httpx.Client(
         base_url=self.BASE_URL,
         follow_redirects=True,
         timeout=10.0
      )

   def get_login_token(self):
      response = self.client.get("/", params={"as":"student"})
      response.raise_for_status()
      soup =  BeautifulSoup(response.text,"html.parser")
      token_element = soup.find("input", {"name" : "_csrf"})
      if token_element is None:
         raise RuntimeError ("UMS Token not Found")
      value = token_element.get("value")
      if value is None:
         raise RuntimeError ("Login Not Successful")
      return value

   def login(self ,uni_roll : str ,password : str):
      token = self.get_login_token()
      data = {
         "roll" : uni_roll,
         "password" : password,
         "_csrf" : token
      }
      response = self.client.post("/student/login.php",data=data)
      response.raise_for_status()
      return response.url.path == "/student/dashboard.php"

   def get_dashboard(self):
      response = self.client.get("student/dashboard.php")
      response.raise_for_status()
      if response.url.path != "/student/dashboard.php":
         raise RuntimeError("UMS Session not authenticated")
      soup = BeautifulSoup(response.text,"html.parser")
      return soup

   def close(self):
      self.client.close()
