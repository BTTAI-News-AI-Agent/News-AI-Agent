from flask import Flask, request, jsonify
from flask_cors import CORS
from models.categorization.categorize import predict_category
from models.summarization.summarization import generate_summary
from models.chatbot.chatbot import setup, askQuestion

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#OpenAI client setup
chat_client = setup()

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
    return response

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
    print("Received summarize request")

    data = request.get_json()
    headline = data.get("headline", "")
    description = data.get("description", "")

    print("Headline:", headline)
    print("Description length:", len(description))

    

    try:
        text = headline + ". " + description
        print("Generating summary...")
        summary = generate_summary(text)
        print("Summary generated!")
        return jsonify({"summary": summary})

    except Exception as e:
        print("SUMMARIZATION ERROR:", e)
        return jsonify({"error": str(e)}), 500


# @app.route("/api/summarize", methods=["POST"])
# def summarize():
#     data = request.get_json()
#     headline = data.get("headline", "")
#     description = data.get("description", "")

#     # combine headline and description for summarization
#     text = headline + ". " + description

#     # call summarization model here
#     from models.summarization.summarization import generate_summary

#     summary = generate_summary(text)
#     # summary = "placeholder summary of the article"

#     return jsonify({"summary": summary})


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}


    headline = data.get("headline", "")
    description = data.get("description", "")
    question = data.get("question", "Summarize the article.")

   
    article = f"Headline: {headline}\n\nDescription: {description}"

    try:
        reply = askQuestion(chat_client, article, question)
        return jsonify({"answer": reply})   #
    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(port=5001, debug=True)
   
  
