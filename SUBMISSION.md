# Submission evidence

All five required emotion tests were executed against the real Watson NLP
service in Skills Network Cloud IDE under `/home/project/final_project`.
The six offline contract tests are recorded separately and use mocks.

| Question | Answer or evidence |
| --- | --- |
| 1 | Public `README.md` URL in this repository |
| 2 | `evidence/2a_emotion_detection.txt` |
| 3 | `evidence/2b_application_creation.txt` |
| 4 | `evidence/3a_output_formatting.txt` |
| 5 | `evidence/3b_formatted_output_test.txt` |
| 6 | Public `EmotionDetection/__init__.py` URL |
| 7 | `evidence/4b_packaging_test.txt` |
| 8 | `evidence/5a_unit_testing.txt` |
| 9 | `evidence/5b_unit_testing_result.txt` |
| 10 | `evidence/6a_server.txt` |
| 11 | `evidence/6b_deployment_test.png` |
| 12 | `evidence/7a_error_handling_function.txt` |
| 13 | `evidence/7b_error_handling_server.txt` |
| 14 | `evidence/7c_error_handling_interface.png` |
| 15 | `evidence/8a_server_modified.txt` |
| 16 | `evidence/8b_static_code_analysis.txt` |

`2b_raw_interactive_transcript.txt` preserves the terminal control characters;
the submitted transcript removes display controls and applies backspaces.
The captured terminal timestamps use the lab host's timezone.

Results: five live tests PASS; six offline tests PASS; pylint `server.py` 10.00/10;
successful web analysis PASS; blank-input web handling PASS; upstream HTTP 400
handling PASS with a mocked response. The browser screenshots show real Flask
responses. No substitute model or hard-coded prediction is used.

The application was implemented with AI assistance. Source and verification
artifacts are supplied for review and reproduction.
