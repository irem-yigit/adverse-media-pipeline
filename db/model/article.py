from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Article:
    url: str
    title: str
    content: str
    published_at: date
    is_adverse: bool
    