import os
import pickle
from typing import Tuple

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "best_news_nb.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "bow_vectorizer.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.pkl")

# Load the pickle files
with open(MODEL_PATH, "rb") as f:
    nb_model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    bow_vectorizer = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)


def predict_category(headline: str, description: str) -> str:
    """
    takes headline, description. returns category 
    """
    
    text = f"{headline} {description}".strip()

    #text -> bag-of-words features
    X = bow_vectorizer.transform([text])

    # BoW -> integer label
    y_int = nb_model.predict(X)[0]

    #integer -> original category string
    category = label_encoder.inverse_transform([y_int])[0]
    return category
