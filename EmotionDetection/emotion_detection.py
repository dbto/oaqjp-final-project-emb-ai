import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        highest_score = 0.0
        dominant_emotion = None
        for emotion, score in emotions.items():
            if score >= highest_score:
                highest_score = score
                dominant_emotion = emotion

        emotions['dominant_emotion'] = dominant_emotion

        return emotions
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
