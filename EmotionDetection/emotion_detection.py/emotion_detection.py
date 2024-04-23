import json 
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers=header, timeout=60)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_scores['anger']
        disgust_score = emotion_scores['disgust']
        fear_score = emotion_scores['fear']
        joy_score = emotion_scores['joy']
        sadness_score = emotion_scores['sadness']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
            'anger': anger_score, 
            'disgust': disgust_score, 
            'fear': fear_score, 
            'joy': joy_score, 
            'sadness': sadness_score, 
            'dominant_emotion': dominant_emotion
            }
