"""
Executing this function initiates the application of emotion 
detector to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detector():
    """
    This function is the route handler for the '/emotionDetector' endpoint. 
    It takes text from the query parameters and passes it to the function
    emotion_detector(). This then returns the analyzed text broken down 
    according to the corresponding emotions. Finally, it returns a text string
    stating the emotions and its scores on the analyzed text.
    """
    text = request.args.get('textToAnalyze')
    analyzed_text = emotion_detector(text)

    if analyzed_text['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    anger_score = analyzed_text['anger']
    disgust_score = analyzed_text['disgust']
    fear_score = analyzed_text['fear']
    joy_score = analyzed_text['joy']
    sadness_score = analyzed_text['sadness']
    dominant_emotion = analyzed_text['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {str(dominant_emotion)}."
    )

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
