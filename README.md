# devops-dashboard

![CI](https://github.com/boozer23/devops-dashboard/actions/workflows/ci.yml/badge.svg)

System monitoring dashboard. Tracks CPU, RAM, and disk usage in real time, runs AI analysis on demand, and fires Telegram alerts when something goes critical.

**Live:** https://devops-dashboard-p6n6.onrender.com

![screenshot](screenshot.png)

## Stack

Python, Flask, psutil, Groq API (LLaMA 3.3), Docker, Kubernetes, Terraform, Prometheus, Grafana, Render

## Run locally

```bash
git clone https://github.com/boozer23/devops-dashboard.git
cd devops-dashboard
pip install -r requirements.txt
export GROQ_API_KEY=your_key
python app.py
```

Open http://localhost:5002

## Docker + Prometheus + Grafana

![grafana](grafana-screenshot.png)

```bash
export GROQ_API_KEY=your_key
docker compose up --build
```

- App: http://localhost:5002
- Prometheus: http://localhost:9091
- Grafana: http://localhost:3000 (admin/admin)

## Kubernetes

![k8s](k8s-screenshot.png)

```bash
minikube start
eval $(minikube docker-env)
docker build -t devops-dashboard:latest .
kubectl create secret generic groq-secret --from-literal=api-key=your_key
kubectl apply -f k8s.yml
minikube service devops-dashboard
```

## Terraform

```bash
cd terraform
terraform init
terraform apply -var="groq_api_key=your_key"
```