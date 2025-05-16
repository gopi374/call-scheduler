import csv
import os
from flask import Flask, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import Client
from datetime import datetime
import pytz

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

log_file = "call_logs.csv"

# ✅ Create the log file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Phone Number", "Message", "Scheduled Time", "Call SID"])

# Twilio credentials (replace with your real values)
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_number = '+YOUR_TWILIO_NUMBER'
to = 'to_receipint_number'
client = Client(account_sid, auth_token)

def make_call(to_number, message):
    from urllib.parse import quote
    response_url = f"https://handler.twilio.com/twiml/EHaa7a66e65bbc68c391ccf1c44a7b1fb2"
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url=response_url
    )
    
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        now = datetime.now().strftime('%Y-%m-%d %I:%M %p')
        writer.writerow([to_number, message, now, call.sid])
        
    print(f"Call scheduled: {call.sid}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule_call():
    data = request.json
    phone = data['phone']
    message = data['message']
    time_str = data['time']

    time_obj = datetime.strptime(time_str, '%H:%M')
    hour, minute = time_obj.hour, time_obj.minute

    # Schedule the call
    scheduler.add_job(make_call, 'cron', hour=hour, minute=minute, args=[phone, message])
    return jsonify({'status': 'success', 'message': 'Call scheduled'})
@app.route('/logs')
def view_logs():
    with open(log_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        logs = list(reader)
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
