from flask import Flask, request
from sentence_transformers import SentenceTransformer
import pickle

app = Flask(__name__)

vectorization_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

with open('model.pkl', 'rb') as f:
    prediction_model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def api():
    text = request.json.get("text")
    if not text:
        return "Unsupported language", 400

    embeddings = vectorization_model.encode(text)

    prediction = prediction_model.predict([embeddings])

    return {"target": float(prediction[0])}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
