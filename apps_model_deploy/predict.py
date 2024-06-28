# import dependencies
import pickle
import pandas as pd
from flask import Flask, request, jsonify

# import model 
with open('numinstalls_lin_reg2.bin', 'rb') as f_in:
    (model) = pickle.load(f_in)  # this loads the rf lr model

# function to prepare new data in format that the model was trained with 
def prepare_features(app_data):
    features = {}   
    features['Category'] = app_data['Category'] 
    features['Type'] = app_data['Type']  
    features['Content_Rating'] = app_data['Content_Rating']  
    features['Size_MBs'] = pd.to_numeric(app_data['Size_MBs'])
    features['Price'] = pd.to_numeric(app_data['Price'])

    return features

# the predicting function 
def predict(features):

    preds = model.predict(features)
   
    return int(preds[0])


# creating a flask application
app =  Flask('number-of-installs-prediction')  # name of the app


# function to use flask app to create web-service for the application.
@app.route('/predict', methods=['POST'])  # adding flask decorator to add extra functionalities from flask framework
def predict_endpoint():
    app_data = request.get_json()

    features = prepare_features(app_data)

    pred = predict(features)

    result = {
        'number-of-installs': pred
    }
    return result

# run the flask application and expose port
if __name__ == "__main__":

    app.run(debug=True, host='localhost', port=9696)


