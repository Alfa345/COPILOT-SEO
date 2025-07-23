# app/advanced_content_analyzer.py
import spacy
from collections import Counter
from .content_analyzer import STOP_WORDS

# Charger le modèle spaCy pour le français
nlp = spacy.load("fr_core_news_sm")

def get_entities(text):
    """Extraire les entités nommées d'un texte."""
    doc = nlp(text)
    return [ent.text for ent in doc.ents]

def get_key_phrases(text, n=10):
    """Extraire les phrases clés d'un texte."""
    doc = nlp(text)
    phrases = [chunk.text for chunk in doc.noun_chunks]
    return Counter(phrases).most_common(n)

def advanced_aggregate_keywords(competitors_data):
    """Agrège, nettoie et classe les mots-clés de tous les concurrents avec une analyse avancée."""
    full_text = ""
    for competitor in competitors_data:
        for heading in competitor.get('headings', []):
            full_text += heading.get('text', '') + " "

    # Extraire les entités et les phrases clés
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
