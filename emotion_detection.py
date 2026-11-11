"""Keep the Task 2 import working after the application is packaged."""

from EmotionDetection.emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
