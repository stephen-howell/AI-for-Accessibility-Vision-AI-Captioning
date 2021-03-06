# AI for Accessibility Vision AI Captioning
This is an Azure Cognitive Services Vision AI Captioning example to accompany a lecture on AI for Accessibility.
As this is a student example, aim is code that is as short and to the point while still being readable. 

## Pre-requirements
Requries Python 3.8 and an Azure subscription.  
If you are a registered student, you can get a free [Azure for Students](https://aka.ms/AzureForStudents) subscription.

In the [Azure Portal](https://portal.azure.com), create a **Computer Vision** resource.  
Select a [pricing tier](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/computer-vision/) (the free F0 tier is fine for this demo).  
Once it is created, go to your new resource and select **Keys and Endpoint**.  
You will need to copy the **KEY 1** and the **Endpoint** for adding to your code later on (keep the key secret and do not upload it to GitHub).  

## Usage
`py caption.py api_version image.png`

_Note: Vision AI API version can be 1.0, 2.0, 2.1, 3.0, 3.1, 3.2 but typically versions 1.0 to 3.0 (inclusive) give exactly the same results, but 3.1, and 3.2 give different results.  
Note: image may be a JPEG or PNG and must be under 4MB_  
