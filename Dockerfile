FROM python:3.11-slim

ARG HF_MODEL_NAME=pjayG25AIT2045/distilbert-imdb-mlops

ENV HF_MODEL_NAME=${HF_MODEL_NAME}

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY inference.py .

CMD ["python", "inference.py"]