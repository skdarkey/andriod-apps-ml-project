import predict
import requests

app_data = {
    "Category" : 'MEDICAL',  #Eg: FINANCE, FAMILY, PARENTING, MEDICAL, GAME, SOCIAL, BUSINESS, PERSONALIZATION
    "Type" : 'Paid',
    "Content_Rating" : 'Teen', # Everyone, Teen, Everyone 10+, 
    "Size_MBs" : '50.0' ,  
    "Price" : '4.99' ,
}

# testing locally
# features = predict.prepare_features(app_data)
# install = predict.predict(features)

# testing on web-service
# url = 'http://localhost:9696/predict'       # local endpoint
url = 'http://13.60.29.10:9696/predict'       # AWS endpoint
response = requests.post(url, json=app_data)
predicted_installs = response.json()

print(f"if the App category is {app_data['Category']} " \
      f"and it is a {app_data['Type']} " \
      f"app and its Content_Rating is {app_data['Content_Rating']} " \
      f"with a Size of about {app_data['Size_MBs']} " \
      f"and Price of {app_data['Price']} " \
      f"then predicted potential number of downloads is {predicted_installs['number-of-installs']}")
