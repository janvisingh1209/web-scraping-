
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from scraper import SCRAPER_REGISTRY

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST', 'OPTIONS'])
def scrape():
    if request.method == 'OPTIONS':
        return jsonify({"status": "OK"}), 200

    data = request.get_json()
    url = data.get('url')

    try:
        # Find matching scraper based on domain
        for domain, scraper_func in SCRAPER_REGISTRY.items():
            if domain in url:
                return jsonify(scraper_func())

        # Default scraper — just scrape paragraphs
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        return jsonify({"type": "paragraphs", "paragraphs": paragraphs})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
