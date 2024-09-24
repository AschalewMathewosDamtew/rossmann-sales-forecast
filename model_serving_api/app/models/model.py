# Define custom transformers before loading the model
class BooleanToInteger:
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.astype(int)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)

import joblib
import os

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Load the trained model with an absolute path
model_path = os.path.join(current_dir, "model-24-09-2024-18-59-21-441214.pkl")
model = joblib.load(model_path)

def predict(feature_1, feature_2):
    # Prepare input data for prediction
    input_data = [[feature_1, feature_2]]
    prediction = model.predict(input_data)
    return prediction[0]  # Return the first prediction