#!/usr/bin/env python
import requests
import os

def synthesise_speech(script):
    body = {'Ocp-Apim-Subscription-Key': os.environ.get("MICROSOFT_KEY")}
    response = requests.post("https://" + os.environ.get("MICROSOFT_REGION") + ".api.cognitive.microsoft.com/sts/v1.0/issuetoken", headers = body)

    print(os.environ.get("MICROSOFT_KEY"))
    print(os.environ.get("MICROSOFT_REGION"))

    print(response.text)
