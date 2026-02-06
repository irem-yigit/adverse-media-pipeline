import requests
from bs4 import BeautifulSoup, soup
from scraper.base_scraper import BaseScraper

class BbcScraper(BaseScraper):

    BASE_URL = "https://www.bbc.com"
    START_URL = "https://www.bbc.com/turkce"

    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

    def get_article_links(self):
        response = requests.get(self.START_URL, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, "lxml")

        links = set()

        for a in soup.select("a[href]"):
            href = a["href"]

            # BBC article pattern
            if "/articles/" in href:
                if href.startswith("/"):
                    links.add(self.BASE_URL + href)


        return list(links)

    def parse_article(self, url):
        response = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, "lxml")

        title = soup.find("h1")
        time = soup.find("time")

        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs)

        return {
            "source": "BBC_TURKCE",
            "url": url,
            "title": title.get_text(strip=True) if title else None,
            "published_at": time.get("datetime") if time else None,
            "content": content
        }
