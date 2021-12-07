#!/usr/bin/env python
import requests
import os

def retrieve_token():
    headers = {'Ocp-Apim-Subscription-Key': os.environ.get("MICROSOFT_KEY")}
    response = requests.post("https://" + os.environ.get("MICROSOFT_REGION") + ".api.cognitive.microsoft.com/sts/v1.0/issuetoken", headers = headers)

    return response.text


def synthesise_speech(script):
    token = retrieve_token()
