import joblib
import os
import numpy as np

# Define custom transformers (needed if these are part of your model pipeline)
class BooleanToInteger:
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.astype(int)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Load the trained model
model_path = os.path.join(current_dir, "model-24-09-2024-18-59-21-441214.pkl")
model = joblib.load(model_path)

# Define a function to test the model
def predict(features):
    # Check if input matches the required number of features (24 in this case)
    if len(features) != 24:
        raise ValueError(f"Expected 24 features, but got {len(features)}")
    
    # Prepare input data for prediction
    input_data = np.array([features])
    prediction = model.predict(input_data)
    return prediction[0]  # Return the first prediction

# Test the model with sample input
if __name__ == "__main__":
    # Example input with 24 features
    features = [1.5, 2.3] + [0] * 22  # Adjust based on your actual features
    try:
        result = predict(features)
        print(f"Prediction: {result}")
    except ValueError as e:
        print(e)
