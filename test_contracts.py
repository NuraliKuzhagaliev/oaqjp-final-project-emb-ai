"""Offline contract and web tests; HTTP responses are explicitly mocked."""

import unittest
from unittest.mock import Mock, patch

import requests

from EmotionDetection.emotion_detection import HEADERS, URL, emotion_detector
from server import app


class TestContracts(unittest.TestCase):
    """Exercise input, transport, formatting, and web error boundaries."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_formatted_output_and_request(self, post):
        """Send the Watson contract and select the highest score."""
        scores = dict(anger=0.8, disgust=0.1, fear=0.2, joy=0.05, sadness=0.3)
        post.return_value = Mock(status_code=200)
        post.return_value.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        self.assertEqual(emotion_detector("I am very angry"),
                         dict(scores, dominant_emotion="anger"))
        post.assert_called_once_with(
            URL, json={"raw_document": {"text": "I am very angry"}},
            headers=HEADERS, timeout=30,
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, post):
        """A provider rejection must return the six-key None result."""
        post.return_value = Mock(status_code=400)
        self.assertEqual(emotion_detector("invalid"), dict.fromkeys(
            ("anger", "disgust", "fear", "joy", "sadness", "dominant_emotion")
        ))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, post):
        """Invalid input must not call the provider."""
        for value in ("", " \n\t", None, 123):
            with self.subTest(value=value):
                result = emotion_detector(value)
                self.assertEqual(len(result), 6)
                self.assertTrue(all(score is None for score in result.values()))
        post.assert_not_called()

    def test_web_blank(self):
        """The real Flask route must show the required input error message."""
        with app.test_client() as client:
            for query in ("", "?textToAnalyze=", "?textToAnalyze=%20%20"):
                response = client.get("/emotionDetector" + query)
                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.text, "Invalid text! Please try again!")
            self.assertEqual(client.get("/").status_code, 200)

    @patch("server.emotion_detector")
    def test_web_success(self, detector):
        """The route must display every score and the dominant emotion."""
        detector.return_value = dict(
            anger=0.01, disgust=0.02, fear=0.03, joy=0.9,
            sadness=0.04, dominant_emotion="joy",
        )
        with app.test_client() as client:
            response = client.get("/emotionDetector?textToAnalyze=I%20am%20glad")
        self.assertEqual(response.status_code, 200)
        self.assertIn("The dominant emotion is joy.", response.text)
        for name in ("anger", "disgust", "fear", "joy", "sadness"):
            self.assertIn("'" + name + "':", response.text)
        detector.assert_called_once_with("I am glad")

    @patch("server.emotion_detector", side_effect=requests.exceptions.Timeout)
    def test_web_service_failure(self, _detector):
        """A timeout must be a service error instead of an input error."""
        with self.assertLogs(app.logger, level="ERROR"):
            with app.test_client() as client:
                response = client.get("/emotionDetector?textToAnalyze=hello")
        self.assertEqual(response.status_code, 503)
        self.assertIn("unavailable", response.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
