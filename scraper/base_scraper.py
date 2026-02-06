from abc import ABC, abstractmethod

class BaseScraper(ABC):

    @abstractmethod
    def get_article_links(self):
        pass

    @abstractmethod
    def parse_article(self, url):
        pass