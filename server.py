
'''
Server for Emotion detection of a given text
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows different emotion score for the provided text.
    '''
    text_to_detect_emotion = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect_emotion)

    if response is None or response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
         f"'anger': {response['anger']}, 'disgust': {response['disgust']},"
         f"'fear': {response['fear']}, 'joy': {[response['joy']]}"
         f"and 'sadness': {response['sadness']}."
         f"The dominant emotion is {response['dominant_emotion']}"
    )


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
