import requests
from bs4 import BeautifulSoup

URL = "https://www.topcv.vn/tim-viec-lam-data-engineer-cr257cb261cl285?category_family=r257~b261l285"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)