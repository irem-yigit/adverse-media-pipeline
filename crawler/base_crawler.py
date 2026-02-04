from abc import ABC, abstractmethod

class BaseCrawler(ABC):

    @abstractmethod
    def fetch_article_links(self):
        pass