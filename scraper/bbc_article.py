import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/turkce/articles/cy4g310ldg7o"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

soup = BeautifulSoup(html, "lxml")

content = []

for p in soup.find_all("p"):
    text = p.get_text(strip=True)
    if text:
        content.append(text)

article_text = " ".join(content)

print(article_text[:1000])
