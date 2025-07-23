# app/__init__.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/analyze', methods=['POST'])
def analyze_keyword():
    try:
        data = request.get_json(force=True)
        keyword = data.get('keyword') if data else None
        if not keyword:
            return jsonify({"error": "Keyword is required"}), 400
        # Mock data
        result = {
            "analysis_summary": {
                "word_count_avg": 1500,
                "common_keywords": [["seo", 5], ["marketing", 4], ["google", 3]],
                "people_also_ask": ["What is SEO?", "How does SEO work?"]
            },
            "ai_generated_outline": "## Introduction\n### What is SEO\n\n## Main Part\n### On-page SEO\n### Off-page SEO\n\n## Conclusion",
            "competitors_detailed": [
                {
                    "title": "Competitor 1 - SEO Guide",
                    "link": "http://example.com/1",
                    "word_count": 1600,
                    "snippet": "A great guide to SEO.",
                    "meta_description": "Learn SEO from scratch.",
                    "headings": [{"tag": "h2", "text": "What is SEO?"}],
                    "alt_tags": ["seo infographic"]
                }
            ],
            "semantic_analysis": {
                "keywords_to_include": [["backlinks", 1], ["serp", 1]]
            },
            "branding": {
                "palette": {
                    "light": {
                        "primary": "#0052CC",
                        "accent": "#FF4F00",
                        "background": "#F7F9FB",
                        "surface": "#FFFFFF",
                        "text": "#1A202C",
                        "success": "#22C55E",
                        "warning": "#FACC15",
                        "error": "#EF4444"
                    },
                    "dark": {
                        "primary": "#3399FF",
                        "accent": "#FF7849",
                        "background": "#181A20",
                        "surface": "#23272F",
                        "text": "#F7F9FB",
                        "success": "#22C55E",
                        "warning": "#FACC15",
                        "error": "#EF4444"
                    }
                },
                "typography": {
                    "heading": "Montserrat",
                    "body": "Inter",
                    "accent": "Space Grotesk"
                },
                "component_style": {
                    "card": "rounded-xl shadow-lg bg-white/80 border border-primary/10 p-6",
                    "button": "rounded-full bg-gradient-to-r from-primary to-accent text-white font-bold px-6 py-2 shadow-md hover:scale-105 transition",
                    "input": "rounded-lg border border-primary focus:ring-2 focus:ring-primary p-3 shadow-sm",
                    "tab": "rounded-t-lg px-4 py-2 font-heading text-primary bg-white/80 shadow transition-colors hover:bg-accent/10",
                    "score_bar": "w-full bg-gray-200 rounded-full h-4 bg-gradient-to-r from-primary to-accent h-4 rounded-full transition-all"
                },
                "layout": "3-column responsive, glassmorphism, sticky side panels, generous spacing, animated transitions",
                "visual_tone": "Audacieux, technologique, épuré, fort contraste, animations, iconographie moderne"
            }
        }
        return jsonify(result)
    except Exception as e:
        print(f"Error in /api/analyze: {e}")
        return jsonify({"error": "Internal server error"}), 500

