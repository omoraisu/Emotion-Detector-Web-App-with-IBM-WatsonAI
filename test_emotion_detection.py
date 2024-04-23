from EmotionDetection.emotion_detection import emotion_detector
import unittest 

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        s1 = emotion_detector("I am glad this happened")
        s2 = emotion_detector("I am really mad about this")
        s3 = emotion_detector("I feel disgusted just hearing about this")
        s4 = emotion_detector("I am so sad about this")
        s5 = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(s1['dominant_emotion'], 'joy')
        self.assertEqual(s2['dominant_emotion'], 'anger')
        self.assertEqual(s3['dominant_emotion'], 'disgust')
        self.assertEqual(s4['dominant_emotion'], 'sadness')
        self.assertEqual(s5['dominant_emotion'], 'fear')
    
unittest.main()