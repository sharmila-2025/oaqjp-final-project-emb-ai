import requests
import json

''' This function uses Watson NLP Library for Emotion Detection
'''
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=request, headers=headers)
    
    json_formatted_response = json.loads(response.text)
    emotion_dict = json_formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion, highest_score = max(emotion_dict.items(), key=lambda item: item[1])
    formatted_response = {
                        'anger': json_formatted_response['emotionPredictions'][0]['emotion']['anger'],
                        'disgust': json_formatted_response['emotionPredictions'][0]['emotion']['disgust'],
                        'fear': json_formatted_response['emotionPredictions'][0]['emotion']['fear'],
                        'joy': json_formatted_response['emotionPredictions'][0]['emotion']['joy'],
                        'sadness': json_formatted_response['emotionPredictions'][0]['emotion']['sadness'],
                        'dominant_emotion': dominant_emotion
                    }
    return formatted_response