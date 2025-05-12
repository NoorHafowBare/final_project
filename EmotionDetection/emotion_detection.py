import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the input text is empty
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = { "raw_document": { "text": text_to_analyze } }

    # Make the request to the emotion API
    response = requests.post(url, headers=headers, json=input_json)

    # Handle errors for unsuccessful requests
    if response.status_code != 200:
        return {"error": "Failed to fetch emotion data"}

    # Parse the response
    response_json = response.json()

    # Check if emotionPredictions are present
    if not response_json.get('emotionPredictions'):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = response_json['emotionPredictions'][0]['emotion']

    # Extracting individual emotion scores
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
