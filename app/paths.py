# app/paths.py

from flask import request, jsonify
import traceback
from app import app

from .serp_analyzer import get_serp_results, scrape_competitor_page
from .ai_assistant import generate_outline_from_competitors, get_chat_response
from .content_analyzer import get_people_also_ask, aggregate_keywords
# app/paths.py
# ... (imports existants) ...

@app.route('/api/analyze-serp', methods=['POST'])
def analyze_serp_route():
    # ... (début de la fonction identique) ...
    
    try:
        # ... (toute la logique d'analyse existante reste la même) ...
        # ... (serp_data, competitors_detailed, people_also_ask, common_keywords, ai_generated_outline) ...

        # --- NOUVELLES DONNÉES EXPERTES ---
        
        # 1. Analyse Sémantique (inspiré de 1.fr)
        # On a déjà `common_keywords`, on va juste le formater pour le frontend
        semantic_analysis = {
            'topic': keyword,
            'keywords_to_include': common_keywords
        }
        
        # 2. Audit de Contenu (simulation inspirée de Quetext)
        # Dans une vraie app, on appellerait une API de détection. Ici, on simule.
        content_audit = {
            'plagiarism_score': 0.0, # Placeholder
            'ai_detection_score': 0.0, # Placeholder
            'readability_score': 0.0 # Placeholder
        }
        
        # 3. Analyse Concurrentielle (inspiré de Detailed SEO extension)
        # On a déjà les données dans `competitors_detailed`, on va juste les passer telles quelles
        
        # --- MISE À JOUR DE LA RÉPONSE JSON ---
        word_counts = [c['word_count'] for c in competitors_detailed if c.get('word_count', 0) > 0]
        avg_word_count = sum(word_counts) / len(word_counts) if word_counts else 0

        analysis_summary = {
            'word_count_avg': round(avg_word_count),
            'common_keywords': common_keywords, # On le garde pour le brief rapide
            'people_also_ask': people_also_ask,
        }

        return jsonify({
            'competitors_detailed': competitors_detailed,
            'analysis_summary': analysis_summary,
            'ai_generated_outline': ai_generated_outline,
            'semantic_analysis': semantic_analysis, # <-- NOUVEAU
            'content_audit': content_audit        # <-- NOUVEAU
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Erreur interne majeure du serveur."}), 500


@app.route('/api/chat', methods=['POST'])
def chat_route():
    # ... (cette fonction est probablement correcte aussi)
    data = request.get_json()
    user_message = data.get('message')
    article_context = data.get('context', '')
    model_name = data.get('model', 'gemini-1.5-flash')
    if not user_message:
        return jsonify({"error": "Message manquant"}), 400
    try:
        response = get_chat_response(user_message, article_context, model_name)
        return jsonify(response)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Erreur interne du serveur dans le chat."}), 500