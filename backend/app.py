from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/api/categorize", methods=["POST"])
def categorize():
    data = request.get_json()
    headline = data.get("headline", "")
    description = data.get("description", "")

    # call categorization model here
    category = "placeholder-category"

    return jsonify({"category": category})

@app.route("/api/summarize", methods=["POST"])
def summarize():
    print("Received summarize request")

    data = request.get_json()
    headline = data.get("headline", "")
    description = data.get("description", "")

    print("Headline:", headline)
    print("Description length:", len(description))

    from models.summarization.summarization import generate_summary

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
    data = request.get_json()
    messages = data.get("chatmessages", [])
    
    #call gpt model here
    reply = "placeholder chat reply"
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
