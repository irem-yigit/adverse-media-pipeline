import requests
from bs4 import BeautifulSoup
from datetime import date

from crawler.base_crawler import BaseCrawler

class BbcCrawler(BaseCrawler):

    BASE_URL = "https://www.bbc.com/turkce"

    def fetch_article_links(self):
        response = requests.get(self.BASE_URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        links = set()

        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]

            if href.startswith("/turkce"):
                full_url = f"https://www.bbc.com{href}"
                links.add(full_url)

        print(f"[Crawler] {len(links)} link bulundu ({date.today()})")
        return list(links)
