# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe7f59d360f1b3ffa1ea4993be02bc810'
auth_token = '529f72a4633945279a7f4051b83202ad'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='hello world!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+59169091721'
                          )

print(message.sid)