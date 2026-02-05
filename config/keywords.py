ADVERSE_KEYWORDS = [
    "terör",
    "uyuşturucu",
    "rüşvet",
    "yolsuzluk", 
    "dolandırıcılık",
    "kara para", 
    "istismar",
    "çocuk istismarı",
    "vergi kaçırma",
    "silah kaçakçılığı",
    "insan kaçakçılığı",
    "terör örgütü"
]

def contains_adverse_keyword(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in ADVERSE_KEYWORDS)
