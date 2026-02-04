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

def is_adverse(text):
    text = text.lower()
    return any(k in text for k in ADVERSE_KEYWORDS)

print(is_adverse(article_text))
