import pickle
import pandas as pd
import numpy as np
model_filename = 'housing_price_predictor.pkl'
print(f"Loading model from {model_filename}...")
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

print("Model loaded successfully!")

# IMPORTANT: The model expects the input data in its original, unscaled format,
# and as a pandas DataFrame with the correct column names.

sample_data = {
    'MedInc': [50],
    'HouseAge': [20],
    'AveRooms': [50],
    'AveBedrms': [50],
    'Population': [500],
    'AveOccup': [7],
    'Latitude': [37.88],
    'Longitude': [-122.23]
}

sample_df = pd.DataFrame(sample_data)
prediction = loaded_model.predict(sample_df)
predicted_price = prediction[0] 
print(f"Predicted Housing Price: ${predicted_price:,.2f}")