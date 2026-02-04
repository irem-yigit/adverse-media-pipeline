from crawler.bbc_crawler import BbcCrawler
from scraper.article_scraper import ArticleScraper
from config.keywords import ADVERSE_KEYWORDS

def contains_adverse_keyword(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in ADVERSE_KEYWORDS)

if __name__ == "__main__":
    crawler = BbcCrawler()
    scraper = ArticleScraper()

    links = crawler.fetch_article_links()

    for link in links[:5]:  # ilk 5 haber
        article = scraper.scrape_article(link)

        if contains_adverse_keyword(article["content"]):
            print("\n[ADVERSE CANDIDATE]")
            print(article["title"])
            print(link)
