import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from textblob import TextBlob  # FREE AI/NLP

def analyze_text(text):
    """AI helper: sentiment + keywords"""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 negative, +1 positive
    keywords = blob.noun_phrases[:5]  # simple keyword extraction
    return {
        "sentiment": "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral",
        "keywords": keywords
    }

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    quotes_data = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]

        # Add AI analysis
        ai = analyze_text(text)

        quotes_data.append({
            "text": text,
            "author": author,
            "tags": tags,
            "ai": ai
        })

    return {"type": "quotes", "quotes": quotes_data}


def scrape_books():
    url = "https://books.toscrape.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').get_text(strip=True)
        image_relative = book.find('img')['src']
        image_url = urljoin(url, image_relative)

        # Add AI analysis for title
        ai = analyze_text(title)

        books.append({
            "title": title,
            "price": price,
            "image": image_url,
            "ai": ai
        })

    return {"type": "books", "books": books}


def scrape_headlines():
    url = "https://news.ycombinator.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    headlines = []
    for item in soup.select('.titleline a'):
        headline = item.get_text(strip=True)

        # Add AI analysis
        ai = analyze_text(headline)

        headlines.append({
            "headline": headline,
            "link": item['href'],
            "ai": ai
        })

    return {"type": "headlines", "headlines": headlines}


# Registry
SCRAPER_REGISTRY = {
    "quotes.toscrape.com": scrape_quotes,
    "books.toscrape.com": scrape_books,
    "news.ycombinator.com": scrape_headlines
}
