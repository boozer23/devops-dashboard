# DevOps Dashboard 📊

Real-time system monitoring dashboard with AI analysis and Telegram alerts.

🌐 **Live Demo**: https://devops-dashboard-p6n6.onrender.com

## 🛠️ Tech Stack

- **Python / Flask** — web server
- **psutil** — system metrics (CPU, RAM, Disk)
- **Groq API (LLaMA 3.3)** — AI analysis
- **Telegram API** — alerts
- **Docker** — containerization
- **Render** — cloud deployment

## 🚀 Quick Start

\`\`\`bash
git clone https://github.com/boozer23/devops-dashboard.git
cd devops-dashboard
pip install -r requirements.txt
export GROQ_API_KEY=your_key
python app.py
\`\`\`

Open http://localhost:5002

## 📁 Project Structure

\`\`\`
devops-dashboard/
├── app.py          # Flask app + metrics + AI analysis
├── index.html      # Frontend dashboard
├── requirements.txt
└── Dockerfile
\`\`\`

## 💡 Features

- Real-time CPU, RAM, Disk monitoring
- Historical charts
- AI-powered system analysis
- Telegram alerts when metrics exceed thresholds