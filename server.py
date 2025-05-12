from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector  # Adjust the path if needed

app = Flask(__name__)

@app.route("/")
def index():
    # Serve the index.html from the templates folder
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    text_to_analyze = request.form['textToAnalyze']
    
    # Call the emotion_detector function to get the emotion analysis result
    result = emotion_detector(text_to_analyze)

    # Handle the case if the emotion detection result is invalid
    if not result:
        return "Invalid input or error with emotion detection service."

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
    app.run(debug=True)  # Run the Flask app in debug mode
