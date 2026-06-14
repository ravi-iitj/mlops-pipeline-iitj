from transformers import pipeline
import os

MODEL_NAME = os.getenv(
    "HF_MODEL_NAME",
    "pjayG25AIT2045/distilbert-imdb-mlops"
)

INPUT_TEXT = os.getenv(
    "INPUT_TEXT",
    "This movie was amazing!"
)

classifier = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME
)

result = classifier(INPUT_TEXT)

print(result)