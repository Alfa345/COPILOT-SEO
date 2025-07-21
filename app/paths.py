# app/paths.py

from flask import request, jsonify
import traceback

# --- Importations corrigées ---
from .serp_analyzer import get_serp_results, scrape_competitor_page
from .ai_assistant import generate_outline_from_competitors # On garde l'outline IA
from .content_analyzer import get_people_also_ask, aggregate_keywords # <-- NOUVEL IMPORT
from app import app

@app.route('/api/analyze-serp', methods=['POST'])
def analyze_serp_route():
    data = request.get_json()
    keyword = data.get('keyword')

    if not keyword:
        return jsonify({"error": "Le mot-clé est manquant"}), 400

    try:
        serp_data = get_serp_results(keyword)
        if 'error' in serp_data:
            return jsonify(serp_data), 500

        competitors_detailed = []
        top_results = serp_data.get('organic_results', [])[:5] # Analyser top 5

        for result in top_results:
            link = result.get('link')
            scraped_data = scrape_competitor_page(link)
            competitors_detailed.append({
                'title': result.get('title'),
                'link': link,
                'snippet': result.get('snippet'),
                'word_count': scraped_data.get('word_count', 0),
                'headings': scraped_data.get('headings', []),
            })

        # --- NOUVELLES ANALYSES DE CONTENU ---
        people_also_ask = get_people_also_ask(keyword)
        common_keywords = aggregate_keywords(competitors_detailed)
        
        # On passe toutes les données à l'IA pour générer le meilleur plan possible
        ai_generated_outline = generate_outline_from_competitors(keyword, competitors_detailed)

        analysis_summary = {
            'word_count_avg': sum(c['word_count'] for c in competitors_detailed) / len(competitors_detailed) if competitors_detailed else 0,
            'common_keywords': common_keywords, # <-- Mots-clés pertinents
            'people_also_ask': people_also_ask, # <-- Questions PAA
        }

        return jsonify({
            'competitors_detailed': competitors_detailed,
            'analysis_summary': analysis_summary,
            'ai_generated_outline': ai_generated_outline
        })

    except Exception as e:
        print(f"--- ERREUR DÉTAILLÉE DANS LA ROUTE ---")
        traceback.print_exc()
        return jsonify({"error": "Erreur interne du serveur lors de l'analyse."}), 500

# La route de chat ne change pas
# ...

        # --- 4. Scrape and analyze each competitor ---
        competitors_detailed = []
        top_results = serp_data.get('organic_results', [])[:3] # Analyze top 3

        for result in top_results:
            link = result.get('link')
            scraped_data = scrape_competitor_page(link)

            # Combine data from SERP and scraping
            competitor_info = {
                'title': result.get('title'),
                'link': link,
                'snippet': result.get('snippet'),
                'word_count': scraped_data.get('word_count', 0),
                'headings': scraped_data.get('headings', []),
            }
            competitors_detailed.append(competitor_info)

        # --- 5. Generate AI outline based on the collected data ---
        # Note: This can take time and should ideally be an async task in a real app
        ai_generated_outline = generate_outline_from_competitors(keyword, competitors_detailed)
        
        # --- 6. Prepare the final JSON response ---
        # (For now, we'll skip the detailed keyword analysis and PAA to simplify and ensure it works)
        analysis_summary = {
            'word_count_avg': sum(c['word_count'] for c in competitors_detailed) / len(competitors_detailed) if competitors_detailed else 0,
            'common_keywords': [], # Placeholder
            'people_also_ask': []  # Placeholder
        }

        return jsonify({
            'competitors_detailed': competitors_detailed,
            'analysis_summary': analysis_summary,
            'ai_generated_outline': ai_generated_outline
        })

    except Exception as e:
        # This will catch any unexpected errors and print them to your terminal
        print(f"--- ERREUR DÉTAILLÉE DANS LA ROUTE ---")
        traceback.print_exc()
        print(f"------------------------------------")
        
        return jsonify({"error": "Erreur interne du serveur lors de l'analyse."}), 500
    
    # app/paths.py
# ... (au début du fichier, avec les autres imports) ...
# ... (imports existants) ...
from .ai_assistant import generate_outline_from_competitors, get_chat_response

# ... (route /api/analyze-serp existante) ...

# --- MODIFICATION DE LA ROUTE CHAT ---
@app.route('/api/chat', methods=['POST'])
def chat_route():
    data = request.get_json()
    user_message = data.get('message')
    article_context = data.get('context', '')
    # On récupère le modèle, avec une valeur par défaut au cas où
    model_name = data.get('model', 'gemini-1.5-flash') 

    if not user_message:
        return jsonify({"error": "Message manquant"}), 400

    # On passe le nom du modèle à notre fonction de l'assistant IA
    response = get_chat_response(user_message, article_context, model_name)
    return jsonify(response)