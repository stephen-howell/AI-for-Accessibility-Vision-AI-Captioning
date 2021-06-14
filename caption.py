import requests
import os.path
import sys
# Add your Computer Vision subscription key 1 and endpoint here
subscription_key = '0000000000000000000000000000'
endpoint = "https://?.cognitiveservices.azure.com/"
# The arguments are api_version to use and image input file name
if len(sys.argv) < 3:
    print("Usage: py caption.py api_version image.png ")
    print("Note: API version can be 1.0, 2.0, 2.1, 3.0, 3.1, 3.2 but typically versions 1.0 to 3.0 inclusive give exactly the same results, but 3.1, and 3.2 give different results")
    print("Note: image may be a JPEG or PNG and must be under 4MB")    
    raise SystemExit
# process the arguments
inputfile = sys.argv[2]
api_version = sys.argv[1]
fileext = os.path.splitext(inputfile)
if os.path.isfile(inputfile):
    if fileext[1] == ".jpg" or fileext[1] =='.png':
        if os.path.getsize(inputfile) < 4194304:
            # Read the image into a byte array
            image_data = open(inputfile, "rb").read()            
            #Set up the headers for the api call
            headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream' }
            params = {'visualFeatures': 'Description'}
            analyze_url = endpoint + "vision/v" + api_version + "/analyze"            
            response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
            response.raise_for_status()
            analysis = response.json()                                                
            vision_caption = str(api_version) + ": "              
            caption = analysis["description"]["captions"][0]
            vision_caption += caption["text"].capitalize()
            vision_caption += " (" + str(round(caption["confidence"] * 100, 1)) + "%)"    
            print(vision_caption)            
        else:
            print("Please specify an image that is 4MB or smaller.")
    else:
        print("Please specify a JPEG or PNG file.")
else:
    print("Please specify a file that exists!")
