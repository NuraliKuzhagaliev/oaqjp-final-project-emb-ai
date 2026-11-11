"""Serve the Watson NLP Emotion Detector web application with Flask."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the text input and emotion analysis interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the supplied text and return scores or a useful error message."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyze)
    except (RequestException, ValueError, KeyError, IndexError, TypeError):
        app.logger.exception("Watson NLP request failed")
        return "Emotion detection service is unavailable. Please try again later.", 503

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
