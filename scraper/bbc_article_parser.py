import requests
from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper
from config.keywords import contains_adverse_keyword


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def parse_article(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    # Başlık
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else None

    # Tarih
    time_tag = soup.find("time")
    published_at = time_tag.get("datetime") if time_tag else None

    # İçerik
    paragraphs = soup.find_all("p")
    content_parts = []

    for p in paragraphs:
        text = p.get_text(strip=True)
        if text:
            content_parts.append(text)

    content = " ".join(content_parts)

    return {
        "title": title,
        "published_at": published_at,
        "content": content
    }


if __name__ == "__main__":
    test_url = "https://www.bbc.com/turkce/articles/cy4g310ldg7o"

    article = parse_article(test_url)

    print("Başlık:", article["title"])
    print("Tarih:", article["published_at"])
    print("İçerik (ilk 500 char):")
    print(article["content"][:500])


if contains_adverse_keyword(article["content"]):
    print("Adverse media olabilir")
else:
    print("Normal haber")
