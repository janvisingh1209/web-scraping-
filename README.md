📌 Project Overview

This project is a web scraping and AI-powered application built with Python Flask for the backend and a simple frontend UI.

1.Scraping Layer

Python + BeautifulSoup scrape quotes/text from a target website.


2.Backend Layer (Flask)

Flask acts as the API backend.

Scraped data is processed and sent to the frontend.

TextBlob is used for AI tasks such as sentiment analysis.


3.AI Integration (TextBlob)

The scraped quotes are passed into TextBlob.

TextBlob analyzes the text (e.g., polarity, subjectivity) or corrects spelling.

Results are sent back to the frontend.


4.Frontend Display

Scraped quotes are displayed in the UI with numbering, size, and color formatting.

Sentiment/analysis results are also shown.
