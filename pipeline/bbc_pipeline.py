from scraper.bbc_scraper import BbcScraper
from scraper.bbc_article_parser import parse_article
from config.keywords import contains_adverse_keyword

def run_bbc_pipeline():
    scraper = BbcScraper()

    for link in scraper.get_article_links():
        article = scraper.parse_article(link)

        if not article["content"]:
            continue

        if contains_adverse_keyword(article["content"]):
            print("Adverse:", article["title"])