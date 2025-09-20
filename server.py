''' Emotion Detection Flask app deployed to localhost:5000
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_analyzer():
    ''' Get text from the HTML interface and runs 
        emotion detector over it.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    return (f"For the given statement, the system response is 'anger': {result['anger']}, " +
             f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} " +
             f"and 'sadness': {result['sadness']}. " +
             f"The dominant emotion is <b>{dominant_emotion}</b>.")

@app.route("/")
def render_index_page():
    ''' Renders the HTML interface
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
