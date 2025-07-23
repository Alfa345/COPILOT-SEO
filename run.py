# In your app.py file

from flask import Flask, request, jsonify
from flask_cors import CORS  # 1. Import CORS here, at the top with other imports

# ... any other imports you have for your analysis logic ...


# This line should already be in your file
app = Flask(__name__)


# 2. Configure CORS right after creating the app instance.
# This is the key change that will fix the "Failed to fetch" error.
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})


# Now, the rest of your app code, like your routes, remains exactly the same.
# For example:
@app.route('/api/analyze', methods=['POST'])
def analyze_keyword():
    # Your existing analysis logic goes here...
    try:
        data = request.get_json()
        keyword = data.get('keyword')
        
        if not keyword:
            return jsonify({"error": "Keyword is required"}), 400

        # Call your actual analysis function here
        # For example: analysis_result = perform_my_analysis(keyword)
        
        # Using the mock data from before to ensure the connection works
        mock_analysis_result = {
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
            }
        }
        
        return jsonify(mock_analysis_result)

    except Exception as e:
        print(f"Error in /api/analyze: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500

# ... any other routes you might have ...