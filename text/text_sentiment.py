from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os

key_var_name = 'TEXT_ANALYTICS_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

endpoint_var_name = 'TEXT_ANALYTICS_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

credentials = CognitiveServicesCredentials(subscription_key)

#Authenticating 
text_analytics = TextAnalyticsClient(endpoint, credentials)

text = input()
documents = [
    {
        'id': '1',
        'text': text
    }
]
response = text_analytics.detect_language(documents = documents)
language_code= response.documents[0].detected_languages[0].iso6391_name



documents = [
    {
        "id": "1",
        "language": language_code,
        "text": text
    }
]
response = text_analytics.sentiment(documents=documents)
if (response.documents[0].score > .5):
    print("You sounds happpy")
elif (response.documents[0].score < .5):
    print("what happened you sounds sad")
else :
   print("ok")

    
