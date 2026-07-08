# devops-dashboard

System monitoring dashboard. Tracks CPU, RAM, and disk usage in real time, runs AI analysis on demand, and fires Telegram alerts when something goes critical.
![CI](https://github.com/boozer23/devops-dashboard/actions/workflows/ci.yml/badge.svg)

**Live:** https://devops-dashboard-p6n6.onrender.com

![screenshot](screenshot.png)

## Stack

Python, Flask, psutil, Groq API (LLaMA 3.3), Docker, Render

## Run locally

```bash
git clone https://github.com/boozer23/devops-dashboard.git
cd devops-dashboard
pip install -r requirements.txt
export GROQ_API_KEY=your_key
python app.py
```

Open http://localhost:5002

## Docker

```bash
docker build -t devops-dashboard .
docker run -p 5002:5002 -e GROQ_API_KEY=your_key devops-dashboard
```

## Kubernetes

```bash
kubectl create secret generic groq-secret --from-literal=api-key=your_key
kubectl apply -f k8s.yml
minikube service devops-dashboard
```