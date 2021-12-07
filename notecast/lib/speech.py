#!/usr/bin/env python
import requests
import os
import boto3
import uuid


def retrieve_token():
    headers = {"Ocp-Apim-Subscription-Key": os.environ.get("MICROSOFT_KEY")}
    response = requests.post(
        "https://"
        + os.environ.get("MICROSOFT_REGION")
        + ".api.cognitive.microsoft.com/sts/v1.0/issuetoken",
        headers=headers,
    )

    return response.text


def synthesise_speech(script):
    token = retrieve_token()
    xml = (
        "<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Male' name='en-GB-SoniaNeural'>"
        + script
        + "</voice></speak>"
    )

    headers = {
        "X-Microsoft-OutputFormat": "audio-48khz-96kbitrate-mono-mp3",
        "User-Agent": "Logpod",
        "Authorization": "Bearer " + token,
        "Content-Type": "application/ssml+xml",
    }

    response = requests.post(
        "https://"
        + os.environ.get("MICROSOFT_REGION")
        + ".tts.speech.microsoft.com/cognitiveservices/v1",
        data=xml,
        headers=headers,
    )

    upload_to_s3(response.content)


def upload_to_s3(file):
    s3 = boto3.resource("s3")
    s3.Bucket("notecast-bucket").put_object(
        Key="casts/" + str(uuid.uuid4()) + ".mp3", Body=file
    )
