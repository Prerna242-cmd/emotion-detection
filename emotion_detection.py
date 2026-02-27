"""
Emotion Detection Module using Watson NLP
"""

import requests

def emotion_detector(text_to_analyse):
    """
    This function sends text to the Watson NLP emotion detection service
    and returns the response in JSON format.
    """

    if not text_to_analyse:
        return None

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    return response.json()
