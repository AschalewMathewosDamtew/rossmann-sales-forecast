import pandas as pd
from flask import Flask, request, jsonify
import joblib
from sklearn.base import TransformerMixin

class BooleanToInteger(TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.astype(int)

app = Flask(__name__)

loaded_pipeline = joblib.load('model-30-09-2024-11-59-13-111256.pkl')

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = loaded_pipeline.predict(input_df)
    return jsonify({'prediction': float(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
