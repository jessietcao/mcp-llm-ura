from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "missing query"}), 400

    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
    res = requests.get(url).json()

    return jsonify({
        "query": query,
        "abstract": res.get("AbstractText", ""),
        "related_topics": [
            t.get("Text")
            for t in res.get("RelatedTopics", [])
            if isinstance(t, dict) and "Text" in t
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

