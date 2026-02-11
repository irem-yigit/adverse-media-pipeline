import psycopg2
from config.database import get_connection
from model.article import Article

class ArticleRepository:

    def save(self, article: Article):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO articles (url, title, content, published_at, is_adverse)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (url) DO NOTHING
        """, (
            article.url,
            article.title,
            article.content,
            article.published_at,
            article.is_adverse
        ))

        conn.commit()
        cur.close()
        conn.close()
