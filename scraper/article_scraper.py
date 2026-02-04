import requests
from bs4 import BeautifulSoup

class ArticleScraper:

    def scrape_article(self, url: str):
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else ""

        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs)

        return {
            "url": url,
            "title": title,
            "content": content
        }
