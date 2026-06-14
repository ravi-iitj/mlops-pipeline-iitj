# End-to-End MLOps Pipeline for Sentiment Analysis

## Overview

This project implements an end-to-end MLOps pipeline for sentiment analysis using the IMDb movie review dataset and the DistilBERT transformer model. The pipeline covers data preprocessing, model training, experiment tracking, model deployment, Docker containerization, and CI/CD automation.

---

## Project Workflow

* Data Preparation and Cleaning
* DistilBERT Model Fine-tuning
* Experiment Tracking with Weights & Biases (W&B)
* Model Deployment to Hugging Face Hub
* Docker Containerization
* CI/CD Automation using GitHub Actions

## Results

Two experiments were performed with different learning rates.

| Metric            | Version 1 | Version 2 |
| ----------------- | --------- | --------- |
| Learning Rate     | 3e-5      | 5e-5      |
| Accuracy          | 0.9050    | 0.9110    |
| Weighted F1 Score | 0.9050    | 0.9110    |
| Validation Loss   | 0.6713    | 0.7467    |

Version 2 achieved the best overall performance and was selected for deployment.

---

## Setup Instructions

### Clone the repository

```bash
git clone https://github.com/ravi-iitj/mlops-pipeline-iitj.git
cd mlops-pipeline-iitj
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the notebook

Open and execute:

```
ml-ops-group-37-project.ipynb
```
## CI/CD Automation

GitHub Actions workflows were implemented for:

- Code quality checks using Flake8 (ci.yml)
- Docker inference workflow validation (inference.yml)

## Docker usage

```bash
- docker pull shrijaya2146/mlops-a3-inference:latest
- docker run --rm shrijaya2146/mlops-a3-inference:latest
```
---

## Public Project Links

### GitHub Repository

https://github.com/ravi-iitj/mlops-pipeline-iitj

## Kaggle Notebook

The notebook contains both experiment versions (LR = 3e-5 and LR = 5e-5), along with data preprocessing, model training, W&B integration, and Hugging Face deployment.

https://www.kaggle.com/code/raviaiethagoni/ml-ops-data-preperation

### Hugging Face Model

https://huggingface.co/pjayG25AIT2045/distilbert-imdb-mlops

### Weights & Biases Dashboard

https://wandb.ai/pinakijayakar01-iitj/mlops-assignment3

### Docker Hub Repository

https://hub.docker.com/r/shrijaya2146/mlops-a3-inference

---

## Technologies Used

* Python
* Hugging Face Transformers
* Kaggle
* Weights & Biases (W&B)
* Docker
* GitHub Actions

---

## Team Members

* A Ravi (Task 1 & Task 2)
* Pinaki Jayakar (Task 3, Task 4 & Task 5)
* Shrijaya Chauhan (Task 6 & Task 7)

---

## Conclusion

This project demonstrates an end-to-end MLOps workflow for sentiment analysis, integrating data preparation, model training, experiment tracking, model hosting, containerization, and CI/CD automation to create a reproducible and deployable machine learning pipeline.
