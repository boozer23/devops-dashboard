# devops-dashboard

System monitoring dashboard. Tracks CPU, RAM, and disk usage in real time, runs AI analysis on demand, and fires Telegram alerts when something goes critical.

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