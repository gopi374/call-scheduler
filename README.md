# 📞 Automated Calling Agent with Twilio and Flask

This is a Python-based automated calling agent that allows users to schedule voice calls using the Twilio API. Built using Flask for the backend and a simple HTML/CSS/JS frontend, the app lets you set a time and message for the call and keeps a log of all scheduled calls.

---

## 🔧 Tech Stack

- **Backend**: Python (Flask)
- **Scheduler**: APScheduler
- **Voice Call API**: Twilio
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: CSV (for call logs)

---

## 🚀 Features

- Schedule automated voice calls using Twilio
- Select time using AM/PM format
- Send custom message in Hindi/English
- Call history logs saved in `call_logs.csv`
- Simple and responsive web interface

---

## 🗂️ Folder Structure
automated-calling-agent/
├── app.py # Main backend logic
├── call_logs.csv # Auto-generated call log file
├── templates/
│ ├── index.html # Schedule call form
│ └── logs.html # View call logs
├── static/
│ ├── style.css # CSS styles
│ └── script.js # JavaScript for frontend
└── README.md # This file

⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/automated-calling-agent.git
cd automated-calling-agent

2. Install required Python packages
pip install flask twilio apscheduler

3. Set up your Twilio credentials
Open app.py and update the following:

account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_number = '+YOUR_TWILIO_PHONE_NUMBER'

4. Run the Flask server
python app.py

6. Expose your local server (Optional)
To receive Twilio webhooks, use ngrok:
Replace the TwiML URL in your code like this:
url = 'https://your-ngrok-url.ngrok.io/voice'
📄 Example TwiML for Custom Voice Message
