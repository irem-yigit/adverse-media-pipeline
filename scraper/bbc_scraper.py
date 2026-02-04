import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.bbc.com"
START_URL = "https://www.bbc.com/turkce"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_article_links():
    response = requests.get(START_URL, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    links = set()

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and href.startswith("/turkce/articles/"):
            links.add(BASE_URL + href)

    return list(links)


if __name__ == "__main__":
    article_links = get_article_links()
    print(f"Toplam link sayısı: {len(article_links)}")

    for link in article_links[:5]:
        print(link)
