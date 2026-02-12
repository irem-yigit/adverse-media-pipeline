from db.repository.article_repository import ArticleRepository
from db.model.article import Article

class ArticleService:

    def __init__(self):
        self.repository = ArticleRepository()

    def save_article(self, article_data: dict, is_adverse: bool, source: str):
        article = Article(
            url=article_data["url"],
            title=article_data["title"],
            content=article_data["content"],
            published_at=article_data["published_at"],
            source=source,
            is_adverse=is_adverse
        )

        self.repository.save(article)
