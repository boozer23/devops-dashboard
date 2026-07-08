from groq import Groq
import os
import psutil
import json
import urllib.request
from flask import Flask, jsonify

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
alert_sent = {"cpu": False, "memory": False, "disk": False}

def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return
    import requests
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})

def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }

def check_alerts(stats):
    global alert_sent
    alerts = []
    if stats["cpu"] > 80 and not alert_sent["cpu"]:
        alerts.append(f"🔴 CPU критично: {stats['cpu']}%")
        alert_sent["cpu"] = True
    elif stats["cpu"] < 70:
        alert_sent["cpu"] = False

    if stats["memory"] > 80 and not alert_sent["memory"]:
        alerts.append(f"🔴 Память критично: {stats['memory']}%")
        alert_sent["memory"] = True
    elif stats["memory"] < 70:
        alert_sent["memory"] = False

    if stats["disk"] > 80 and not alert_sent["disk"]:
        alerts.append(f"🔴 Диск критично: {stats['disk']}%")
        alert_sent["disk"] = True
    elif stats["disk"] < 70:
        alert_sent["disk"] = False

    if alerts:
        send_telegram("⚠️ DevOps Alert!\n\n" + "\n".join(alerts))

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/stats")
def stats():
    s = get_system_stats()
    check_alerts(s)
    return app.response_class(
        response=json.dumps(s, ensure_ascii=False),
        mimetype='application/json'
    )

@app.route("/analyze")
def analyze():
    s = get_system_stats()
    prompt = f"CPU: {s['cpu']}%, Память: {s['memory']}%, Диск: {s['disk']}%. Проанализируй коротко — 2-3 предложения на русском."
    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    return app.response_class(
        response=json.dumps({"ai_analysis": chat.choices[0].message.content}, ensure_ascii=False),
        mimetype='application/json'
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
