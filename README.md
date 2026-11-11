# Final Project

## Emotion Detection using Watson NLP and Flask

Analyze English text for anger, disgust, fear, joy and sadness using IBM's
Embeddable Watson NLP EmotionPredict service. Returns all five scores and the
dominant emotion. Blank input and HTTP 400 return six `None` values; the web
interface displays `Invalid text! Please try again!`. Upstream failures return 503.

### Run in Skills Network Cloud IDE

```bash
cd /home/project
git clone https://github.com/NuraliKuzhagaliev/oaqjp-final-project-emb-ai.git final_project
cd final_project
python3 -m pip install -r requirements-dev.txt
python3 server.py
```

Open the port 5000 preview. The Watson endpoint is provided by Skills Network
and may only be accessible from the course laboratory environment.

### Verify

```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
python3 test_emotion_detection.py
python3 -m unittest test_contracts -v
python3 -m pylint server.py
```

`test_emotion_detection.py` calls real Watson for the five required statements.
`test_contracts.py` uses explicitly mocked HTTP responses to check formatting,
request structure, error handling and Flask routing offline.

### Files

- `EmotionDetection/emotion_detection.py`: Watson client and formatted output.
- `EmotionDetection/__init__.py`: package export.
- `emotion_detection.py`: Task 2 compatibility import.
- `server.py`: Flask routes.
- `templates/`, `static/`: browser interface based on the IBM starter project.
- `evidence/`: code, terminal output and screenshots for the 16 questions.

Based on the Apache-2.0 licensed IBM Developer Skills Network starter repository.
