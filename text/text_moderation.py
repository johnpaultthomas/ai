import http.client,urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Content-Type': 'text/plain',
    'Ocp-Apim-Subscription-Key': '7152881e888145ee8b00e33e3f1f421d',
}

print ("Hello there..")

body = input()
params = urllib.parse.urlencode({'classify': True})

try:
    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
    conn.request("POST",
    "/contentmoderator/moderate/v1.0/ProcessText/Screen?%s" %
    params, body , headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
   
    #print (data["Classification"]["ReviewRecommended"])
    #print ((data["Terms"][0])["Term"])
    if((data["Classification"]["ReviewRecommended"])):
            if(((data["Terms"][0])["Term"]) is None):
                print ("Mind your language")
            else:
                print("I am not a",(data["Terms"][0])["Term"] , "you moron")
    else:
        print ("I could not understand you")
    conn.close()
except Exception as e:
    print("Error")
    print(data)
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))
