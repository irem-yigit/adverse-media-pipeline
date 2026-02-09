import requests
from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper
from config.scraper_config import BBC_BASE_URL, REQUEST_TIMEOUT

class BbcScraper(BaseScraper):

    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

    def get_article_links(self):
        try:
            response = requests.get(BBC_BASE_URL, timeout=REQUEST_TIMEOUT, headers=self.HEADERS)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"BBC bağlantı hatası: {e}")
            return []

        soup = BeautifulSoup(response.text, "lxml")
        links = set()

        for a in soup.select("a[href]"):
            href = a["href"]

            # BBC article pattern
            if "/articles/" in href:
                if href.startswith("/"):
                    full_url = self.BASE_URL + href
                else:
                    full_url = href

                links.add(full_url)

        return list(links)

    def parse_article(self, url):
        try:
            response = requests.get(url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Haber çekilemedi: {url} -> {e}")
            return None

        soup = BeautifulSoup(response.text, "lxml")

        # Başlık
        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else None

        # Tarih
        time_tag = soup.find("time")
        published_at = time_tag.get("datetime") if time_tag else None

        # Asıl article body'yi bulmaya çalış
        article_tag = soup.find("article")

        if article_tag:
            paragraphs = article_tag.find_all("p")
        else:
            paragraphs = soup.find_all("p")

        content_parts = []
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                content_parts.append(text)

        content = " ".join(content_parts)

        if not content:
            return None

        return {
            "source": "BBC_TURKCE",
            "url": url,
            "title": title,
            "published_at": published_at,
            "content": content
        }
