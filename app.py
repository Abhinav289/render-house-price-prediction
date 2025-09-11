import pickle
from flask import Flask, request, app, jsonify, render_template
import numpy as np
import pandas as pd
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

try:
    model = pickle.load(open('housing_price_predictor.pkl', 'rb'))
    logging.info("Model loaded successfully.")
except FileNotFoundError:
    model = None
    logging.error("Model file 'housing_price_predictor.pkl' not found.")
except Exception as e:
    model = None
    logging.error(f"An error occurred while loading the model: {e}")

# model = pickle.load(open('housing_price_predictor.pkl','rb'))
@app.route('/')

def homepage():
    return render_template('home.html')



@app.route('/predict',methods=['POST'])
def predict():
    if model is None:
        return render_template('home.html', prediction_text='Error: Model is not loaded. Please check the server logs.')
    
    try:
        feature_names = [
            'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
            'Population', 'AveOccup', 'Latitude', 'Longitude'
        ]
        data = {name: [float(request.form[name])] for name in feature_names}
        input_df = pd.DataFrame(data)

        logging.info(f"Input DataFrame for prediction:\n{input_df}")
        prediction = model.predict(input_df)
        output=prediction[0]
       
        print(output)
        
        final_price = output
        formatted_prediction = f"${final_price:,.2f}"
        return render_template("home.html",prediction_text=f"The predicted House price  is {formatted_prediction}")
    except ValueError:
         return render_template('home.html', prediction_text='Error: Please enter valid numbers for all features.')
    except Exception as e:
        logging.error(f"An error occurred during prediction: {e}")
        return render_template('home.html', prediction_text='An unexpected error occurred. Please try again.')



if __name__ == '__main__':
    app.run(debug=True)
