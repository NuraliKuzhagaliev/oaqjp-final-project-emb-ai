"""Detect five emotions in English text using the Watson NLP service."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return five scores and the dominant emotion; invalid input returns None.

    Watson HTTP 400 responses use the same six-key empty result as blank input.
    Network errors, other HTTP failures, and malformed responses propagate so
    callers can distinguish a service failure from an invalid statement.
    """
    empty_result = dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result

    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyze}},
        headers=HEADERS,
        timeout=30,
    )
    if response.status_code == 400:
        return empty_result
    response.raise_for_status()
    scores = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
