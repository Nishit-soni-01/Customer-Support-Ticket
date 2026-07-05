# Customer Support Ticket Triage System

An AI-powered Natural Language Processing (NLP) web application built to automatically classify and route incoming customer support tickets into optimized department lanes. The application leverages a machine learning pipeline to analyze text descriptions and accurately categorize them in real-time.

Built with a production-first mindset, the system is fully containerized using Docker and optimized for secure, scalable serverless deployment on AWS ECS Fargate.

---

## 🚀 Features
* **Automated Triage Engine:** Classifies tickets instantly into 5 distinct categories: *Technical issue*, *Billing inquiry*, *Product inquiry*, *Cancellation request*, and *Refund request*.
* **Interactive Web Dashboard:** A clean, minimalistic Flask front-end interface built to take user input and display categorized routing lanes dynamically.
* **Production-Grade Architecture:** Upgraded security configurations utilizing non-root users, unbuffered logging streams, and optimized Gunicorn multi-threading configurations.
* **Cloud-Ready Containerization:** Completely packaged using Docker with optimized layer caching and explicit `.dockerignore` boundary rules to prevent local virtual environment clutter.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Framework:** Flask, Gunicorn
* **Machine Learning & NLP:** Scikit-Learn (TF-IDF Vectorizer + Random Forest Classifier), NLTK
* **DevOps & Cloud:** Docker, AWS ECR, AWS ECS Fargate

---

## 📦 Project Directory Structure
```text
Customer Support Ticket/
├── .dockerignore              # Prevents massive venv layers in Docker builds
├── .gitignore                 # Keeps Git repository clean
├── Dockerfile                 # Production-optimized multi-thread Docker configuration
├── application.py             # Main Flask application entry point
├── requirements.txt           # Explicit python project dependencies
├── setup.py                   # Package installation configurations
├── artifacts/                 # Saved trained ML model and vectorizer binaries
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── label_encoder.pkl
├── notebook/                  # Jupyter notebooks for EDA and model exploration
│   └── 1_EDA_and_Model_Training.ipynb
├── src/                       # Modular pipeline implementation source code
│   ├── components/
│   └── pipeline/
└── templates/                 # HTML UI layouts for the web dashboard