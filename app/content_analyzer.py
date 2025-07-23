# app/content_analyzer.py
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import spacy

# Load the spaCy model for French
nlp = spacy.load("fr_core_news_sm")

STOP_WORDS = set([
    'le', 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'et', 'ou', 'est', 'sont',
    'pour', 'par', 'sur', 'dans', 'avec', 'ce', 'cette', 'ces', 'qui', 'que',
    'quoi', 'dont', 'où', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'je',
    'tu', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses', 'notre',
    'votre', 'leur', 'leurs', 'au', 'aux', 'pas', 'plus', 'comment', 'votre',
    'pourquoi', 'quand', 'quel', 'quelle', 'quelles', 'quels', 'aussi', 'si',
    'tout', 'tous', 'bien', 'faire', 'peut'
])

def get_entities(text):
    """Extraire les entités nommées d'un texte."""
    doc = nlp(text)
    return [ent.text for ent in doc.ents]

def get_key_phrases(text, n=10):
    """Extraire les phrases clés d'un texte."""
    doc = nlp(text)
    phrases = [chunk.text for chunk in doc.noun_chunks]
    return Counter(phrases).most_common(n)

def aggregate_keywords(competitors_data):
    """Agrège, nettoie et classe les mots-clés de tous les concurrents avec une analyse avancée."""
    full_text = ""
    for competitor in competitors_data:
        for heading in competitor.get('headings', []):
            full_text += heading.get('text', '') + " "

    # Extract entities and key phrases
    entities = get_entities(full_text)
    key_phrases = get_key_phrases(full_text)

    # Nettoyer et compter les mots
    words = [word for word in full_text.lower().split() if word not in STOP_WORDS and len(word) > 2]
    word_counts = Counter(words).most_common(15)

    return {
        'entities': entities,
        'key_phrases': key_phrases,
        'word_counts': word_counts
    }

def get_people_also_ask(keyword):
    """Récupère les questions 'People Also Ask' pour un mot-clé donné."""
    questions = []
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        response = requests.get(f"https://www.google.com/search?q={keyword}&hl=fr", headers={'User-Agent': user_agent})

        soup = BeautifulSoup(response.text, 'html.parser')

        paa_container = soup.find('div', attrs={'data-initq': keyword, 'data-rw': True})
        if paa_container:
            questions_divs = paa_container.find_all('div', role='heading')
            for div in questions_divs:
                questions.append(div.get_text(strip=True))
    except Exception as e:
        print(f"Erreur lors de la récupération des PAA : {e}")
    return list(set(questions))[:4]
