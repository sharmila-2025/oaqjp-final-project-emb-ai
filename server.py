from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def text_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    formatted_response = emotion_detector(text_to_analyze)

    dominant_emotion = formatted_response['dominant_emotion']
    emotions = formatted_response.pop('dominant_emotion')

    return "For the given statement, the system response is {}. The dominant emotion is{}.".format(emotions, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)