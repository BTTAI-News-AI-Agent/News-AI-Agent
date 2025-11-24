from flask import Flask, render_template, request, jsonify, flash,redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(2354)  #needed to keep sessions and flashing

article = "" #should make a database instead, this will cause problems 

def chatbot_response(user_input):
    return "chat response" # copy from prev. milestone

def summarize_article(article):
    return f"summary of the article is htis." # copy from prev. milestone

def categorize_article(article):
    return "The category is []"  #call classificaton function

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

@app.route("/summarize", methods=["POST"])
def summarize():
    article = request.json.get("article")
    summary = summarize_article(article)
    return jsonify({"summary": summary})

@app.route("/categorize", methods=["POST"])
def categorize():
    article = request.json.get("article")
    category = categorize_article(article)
    return jsonify({"category": category})

@app.route("/article", methods=["POST"])
def submit_article():
    input = request.json.get("article")
    global article
    article = input
    flash("article received")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
