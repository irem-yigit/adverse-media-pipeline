import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/turkce/articles/cj4ljjk2n0xo"

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

KEYWORDS = [
    "terör", "uyuşturucu", "rüşvet",
    "yolsuzluk", "dolandırıcılık",
    "kara para", "istismar"
]

def is_adverse(text):
    text = text.lower()
    return any(k in text for k in KEYWORDS)

print(is_adverse(article_text))

