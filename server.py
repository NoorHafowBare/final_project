"""Flask web application for emotion detection.

This module provides a Flask web interface for analyzing emotions in text input.
It includes routes for serving the main page and processing emotion detection requests.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector  # Adjust the path if needed

# Create an instance of the Flask class
app = Flask(__name__)

@app.route("/")
def index():
    """Route to serve the index page.
    
    Returns:
        str: The index.html template from the templates folder.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """Route to handle emotion detection requests.
    
    Receives a POST request with text input, processes it using emotion_detector,
    and returns formatted output with detected emotions.
    
    Returns:
        str: Formatted output showing detected emotions and dominant emotion.
        JSON: Error message if input is invalid or emotion detection fails.
    """
    # Get the input text from the form
    text_to_analyze = request.form['textToAnalyze']
    # Handle blank or invalid input
    if not text_to_analyze.strip():
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # If the result is invalid
    if not result or 'error' in result:
        return jsonify({"error": "Failed to fetch emotion data"}), 400

    # Prepare the formatted response
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_output

if __name__ == "__main__":
    # Entry point to run the Flask application
    app.run(debug=True)
    