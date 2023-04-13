from twilio.rest import Client

# Your Twilio account SID and auth token (find these in your Twilio dashboard)
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define your Twilio phone number and the phone number you want to call
from_phone_number = '+1234567890'  # Your Twilio phone number
to_phone_number = '+0987654321'    # The phone number you want to call

# Define the URL of the XML file containing TwiML instructions
# Replace "yourserver.com" with the domain where you host your TwiML XML file
twiml_url = 'https://yourserver.com/twiml.xml'

# Make the voice call
call = client.calls.create(
    url=twiml_url,
    to=to_phone_number,
    from_=from_phone_number,
)

print(f'Call initiated. Call SID: {call.sid}')
