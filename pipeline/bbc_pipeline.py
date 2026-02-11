import logging
from scraper.bbc_scraper import BbcScraper
from config.keywords import contains_adverse_keyword
from datetime import timedelta,datetime

logger = logging.getLogger(__name__)

def run_bbc_pipeline():
    scraper = BbcScraper()
    today = datetime.today().date()

    for link in scraper.get_article_links():
        article = scraper.parse_article(link)

        if not article["content"] or not article["published_at"]:
            continue

        article_date = datetime.strptime(
            article["published_at"], "%Y-%m-%d"
        ).date()

        # Only consider articles published in the last 24 hours
        if article_date < today - timedelta(days=1):
            continue

        if contains_adverse_keyword(article["content"]):
            logging.info("Adverse: %s", article["title"])
