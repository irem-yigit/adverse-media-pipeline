import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/turkce"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(response.text, "lxml")

headlines = soup.find_all("a")

for h in headlines[:10]:
    print(h.get_text(strip=True))
