from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import Client

account_sid = 'AC3215504ab9f01aed383360c64ceb7303'
auth_token = '63685cfe6fb5cb07947a587e74ea3127'
twilio_number = '+12179553121'
to_number = '+91 7389600475'

client = Client(account_sid, auth_token)

def make_call():
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url='https://handler.twilio.com/twiml/EHaa7a66e65bbc68c391ccf1c44a7b1fb2'  # Replace with your custom voice URL
    )
    print(f"Call made. SID: {call.sid}")

scheduler = BlockingScheduler()
scheduler.add_job(make_call, 'cron', hour=22, minute=51)  # ⏰ Runs daily at 9:30 AM

print("Call scheduler started.")
scheduler.start()
