# app/content_analyzer.py

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

# Liste de "stop words" français très basique pour nettoyer le bruit
STOP_WORDS = set([
    'le', 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'et', 'ou', 'est', 'sont',
    'pour', 'par', 'sur', 'dans', 'avec', 'ce', 'cette', 'ces', 'qui', 'que',
    'quoi', 'dont', 'où', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'je',
    'tu', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses', 'notre',
    'votre', 'leur', 'leurs', 'au', 'aux', 'pas', 'plus', 'comment', 'votre',
    'pourquoi', 'quand', 'quel', 'quelle', 'quelles', 'quels', 'aussi', 'si',
    'tout', 'tous', 'bien', 'faire', 'peut'
])

def get_people_also_ask(keyword):
    """Récupère les questions "People Also Ask" pour un mot-clé donné."""
    questions = []
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        response = requests.get(f"https://www.google.com/search?q={keyword}&hl=fr", headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Google utilise des divs avec des rôles spécifiques pour PAA
        paa_container = soup.find('div', attrs={'data-initq': keyword, 'data-rw': True})
        if paa_container:
            questions_divs = paa_container.find_all('div', role='heading')
            for div in questions_divs:
                questions.append(div.get_text(strip=True))

    except Exception as e:
        print(f"Erreur lors de la récupération des PAA : {e}")
    return list(set(questions))[:4] # Retourne 4 questions uniques

def aggregate_keywords(competitors_data):
    """Agrège, nettoie et classe les mots-clés de tous les concurrents."""
    full_text = ""
    for competitor in competitors_data:
        # On utilise le texte des titres pour l'analyse sémantique
        for heading in competitor.get('headings', []):
            full_text += heading.get('text', '') + " "
            
    # Nettoyer et compter les mots
    words = re.findall(r'\b\w{3,}\b', full_text.lower())
    
    # Filtrer les stop words
    filtered_words = [word for word in words if word not in STOP_WORDS]
    
    word_counts = Counter(filtered_words)
    return word_counts.most_common(15) # Retourne les 15 mots-clés sémantiques les plus pertinents