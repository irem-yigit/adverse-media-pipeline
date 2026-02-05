from scraper.bbc_scraper import get_article_links
from scraper.bbc_article_parser import parse_article
from config.keywords import contains_adverse_keyword

links = get_article_links()

for link in links[:10]:
    article = parse_article(link)

    if not article["content"]:
        continue

    if contains_adverse_keyword(article["content"]):
        print("\n--- ADVERSE HABER ---")
        print(article["title"])
        print(link)
