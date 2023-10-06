from flask import Flask, render_template, request, jsonify
import pickle
from utils import model_predict

app = Flask(__name__, template_folder='templates')
cv = pickle.load(open("models/cv.pkl", "br"))
clf = pickle.load(open("models/clf.pkl", "br"))


@app.route("/")
def home():
    return render_template("index.htm")


@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get('content')
    prediction = model_predict(email)
    return render_template("index.htm", prediction=prediction, email=email)


@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    email = data['content']
    prediction = model_predict(email=email)
    return jsonify({'prediction': prediction, 'email':email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
