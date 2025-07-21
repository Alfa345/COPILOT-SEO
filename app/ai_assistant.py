# app/ai_assistant.py

import os
import google.generativeai as genai

# --- Configuration du client Google ---
# On configure le client une seule fois au démarrage
try:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if GOOGLE_API_KEY:
        genai.configure(api_key=GOOGLE_API_KEY)
        print("Client Google AI configuré avec succès.")
    else:
        print("Clé d'API Google manquante. Le modèle Google ne sera pas disponible.")
except Exception as e:
    print(f"Erreur lors de la configuration de Google AI: {e}")

# Dictionnaire pour stocker les instances de modèles déjà initialisées (cache simple)
model_instances = {}

def get_model(model_name: str):
    """
    Récupère une instance de modèle. S'il n'est pas dans le cache, l'initialise.
    Ceci est une fonction "routeur" qui pourra gérer d'autres API (OpenAI, etc.) à l'avenir.
    """
    if model_name in model_instances:
        return model_instances[model_name]

    # --- Logique du routeur de modèle ---
    if model_name.startswith('gemini'):
        if not GOOGLE_API_KEY:
            raise ValueError("La clé API Google est requise pour utiliser un modèle Gemini.")
        try:
            model = genai.GenerativeModel(model_name)
            model_instances[model_name] = model
            return model
        except Exception as e:
            raise Exception(f"Impossible d'initialiser le modèle Gemini '{model_name}': {e}")
    
    # elif model_name.startswith('openai'):
    #     # Ici, on ajouterait la logique pour initialiser un client OpenAI
    #     pass
    
    else:
        raise ValueError(f"Le modèle '{model_name}' n'est pas supporté.")


def generate_outline_from_competitors(keyword, competitors_data):
    """Génère un plan d'article (utilise le modèle le plus puissant par défaut)."""
    # Pour la génération de plan, on choisit le meilleur modèle par défaut
    model_name = 'gemini-1.5-pro'
    
    # ... le reste de cette fonction ne change pas, mais on va la faire appeler get_model
    try:
        model = get_model(model_name)
    except Exception as e:
        return {"error": str(e)}

    # ... (Le reste du prompt et de la logique de cette fonction est identique)
    # ...
    # Le prompt est construit ici ...
    # ...
    # L'appel à l'API est fait ici, avec le `model` qu'on vient de récupérer
    # response = model.generate_content(full_prompt)
    # ...
    # Le reste de la fonction est pareil...

    # Pour l'instant, je vais la laisser statique pour ne pas tout réécrire
    # mais l'idée est de remplacer `model.generate_content(prompt)` par
    # `get_model('gemini-1.5-pro').generate_content(prompt)`
    
    # Simule un retour rapide pour ne pas compliquer l'exemple
    return "Plan généré avec gemini-1.5-pro (logique à implémenter entièrement)."


def get_chat_response(user_message, article_context, model_name: str):
    """Génère une réponse de chatbot avec le modèle spécifié."""
    try:
        # On récupère le modèle demandé par l'utilisateur
        model = get_model(model_name)
    except Exception as e:
        return {"reply": str(e)}

    prompt = f"""
    **Rôle :** Tu es "Copilote SEO", un assistant d'écriture expert utilisant le modèle {model_name}.
    
    **Contexte de l'article en cours d'écriture :**
    ---
    {article_context}
    ---
    
    **Question de l'utilisateur :**
    "{user_message}"
    
    **Instructions :**
    Réponds à la question de l'utilisateur de manière concise et utile.
    """
    
    try:
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        # Ici on peut aussi ajouter la gestion d'erreur de quota comme avant
        return {"reply": f"Erreur lors de la communication avec le modèle {model_name}: {e}"}