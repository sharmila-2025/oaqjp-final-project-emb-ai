"""An applicaiton to get the type of emotion for given text"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def text_emotion_detector():
    """Call emotion detector to determine the dominent emotion"""
    text_to_analyze = request.args.get('textToAnalyze')

    formatted_response = emotion_detector(text_to_analyze)

    dominant_emotion = formatted_response.pop('dominant_emotion')
    emotions = (str(formatted_response)).replace('{','').replace('}','')

    if dominant_emotion == 'None':
        return "Invalid text!"

    all_emotions = f"For the given statement, the system response is {emotions}. "
    dominant_emotion_res = f"The dominant emotion is {dominant_emotion}."
    return  all_emotions + dominant_emotion_res

@app.route("/")
def render_index_page():
    """Render index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
