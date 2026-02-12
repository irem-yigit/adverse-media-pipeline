import logging
from scraper.bbc_scraper import BbcScraper
from config.keywords import contains_adverse_keyword
from datetime import timedelta,datetime
from db.service.article_service import ArticleService

logger = logging.getLogger(__name__)

def run_bbc_pipeline():
    scraper = BbcScraper()
    service = ArticleService()
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

        is_adverse = contains_adverse_keyword(article["content"])

        service.save_article(article, is_adverse)

        if is_adverse:
            logger.info(f"Adverse saved: {article['title']}")
