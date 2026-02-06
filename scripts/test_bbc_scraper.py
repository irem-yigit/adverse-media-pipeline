import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.bbc_scraper import BbcScraper

def test_get_article_links():
    scraper = BbcScraper()
    links = scraper.get_article_links()

    print(f"Toplam link sayısı: {len(links)}")

    for link in links[:5]:
        print(link)

def test_parse_single_article():
    scraper = BbcScraper()
    links = scraper.get_article_links()

    if not links:
        print(" Link bulunamadı")
        return

    article = scraper.parse_article(links[0])

    print("\n--- PARSED ARTICLE ---")
    print("Title:", article.get("title"))
    print("Date:", article.get("published_at"))
    print("Content (first 300 chars):")
    print(article.get("content")[:300])

if __name__ == "__main__":
    test_get_article_links()
    test_parse_single_article()
