import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/turkce"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(response.text, "lxml")

links = []

for a in soup.find_all("a"):
    href = a.get("href")
    if href and "/turkce/articles/" in href:
        links.append("https://www.bbc.com" + href)

print("Toplam link:", len(set(links)))

for link in list(set(links))[:5]:
    print(link)
