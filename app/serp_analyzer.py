# app/serp_analyzer.py
import requests
import os
from bs4 import BeautifulSoup

API_KEY = os.getenv("VALUESERP_API_KEY")
BASE_URL = "https://api.valueserp.com/search"

def get_serp_results(keyword):
    """Same as before"""
    pass

def scrape_competitor_page(url):
    if not url:
        return {'error': 'URL manquante.'}
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')

        main_content = soup.find('article') or soup.find('main') or soup.body
        text = main_content.get_text(separator=' ', strip=True) if main_content else ""
        word_count = len(text.split())

        headings = [{'tag': h.name, 'text': h.get_text(strip=True)} for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

        # Extract meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_description = meta_description['content'] if meta_description else ""

        # Extract image alt tags
        images = soup.find_all('img')
        alt_tags = [img.get('alt', '') for img in images if img.get('alt')]

        return {
            'word_count': word_count,
            'headings': headings,
            'meta_description': meta_description,
            'alt_tags': alt_tags
        }
    except Exception as e:
        return {'word_count': 0, 'headings': [], 'error': f'Erreur de scraping sur {url}: {e}', 'meta_description': "", 'alt_tags': []}
