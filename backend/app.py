from flask import Flask, request, jsonify
from flask_cors import CORS
from models.categorization.categorize import predict_category
from models.chatbot.chatbot import setup, askQuestion

app = Flask(__name__)
CORS(app)  
client = setup()

@app.route("/api/categorize", methods=["POST"])
def categorize():
    data = request.get_json()
    headline = data.get("headline", "")
    description = data.get("description", "")

    # call predict_category from categorization.py
    category = predict_category(headline, description)

    return jsonify({"category": category})


@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    headline = data.get("headline", "")
    description = data.get("description", "")

    # Using GPT Summarization
    summary = askQuestion(
        client,
        description,
        question="Summarize the article in 3–5 sentences."
    )

    return jsonify({"summary": summary})


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("chatmessages", [])
    
    #call gpt model here
    reply = "placeholder chat reply"
    return jsonify({"reply": reply})


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(port=5000, debug=True)
