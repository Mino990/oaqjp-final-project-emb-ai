from EmotionDetection.emotion_detection import emotion_detector

import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    """Unit test class for SA"""
    def test_emotion_analyzer(self):
        """Unit test cases for sentiment analysis"""
        #joy
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        #Anger
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

        #Disgust
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        #Sadness
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

        #Fear
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')



unittest.main()