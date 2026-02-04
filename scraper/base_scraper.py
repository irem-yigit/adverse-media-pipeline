from abc import ABC, abstractmethod

class BaseScraper(ABC):

    @abstractmethod
    def scrape_article(self, url: str):
        pass