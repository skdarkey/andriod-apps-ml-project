import predict
import requests

# testing before webservice
app_data = {
    "Category" : 'GAME',  #Eg: FINANCE, FAMILY, PARENTING, MEDICAL, GAME, SOCIAL, BUSINESS, PERSONALIZATION
    "Type" : 'Paid',
    "Content_Rating" : 'Teen', # Everyone, Teen, Everyone 10+, 
    "Size_MBs" : '15.0' ,  
    "Price" : '5' ,
}

# testing locally
# features = predict.prepare_features(app_data)
# install = predict.predict(features)

# testing on web-service
url = 'http://localhost:9696/predict'    # specify the endpoiint "predict" which is used in the flask app
response = requests.post(url, json=app_data)
print(response.json())

