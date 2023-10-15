import os
import smtplib

# Credential initialization
_SENDER = _RECIPIENT = os.getenv('EMAIL_ACC')
_PASSWORD = os.getenv('EMAIL_APP_PASSWD')
assert _SENDER,   'EMAIL_ACC environment variable does not exist.'
assert _PASSWORD, 'EMAIL_APP_PASSWD environment variable does not exist.'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


sender_email = _SENDER
sender_password = _PASSWORD
recipient_email = _RECIPIENT
subject = "Hello from Python"
body = "<html><body><h1>with image</h1><img src=https://a.espncdn.com/i/teamlogos/nfl/500/buf.png height=125px/></body></html>"

# with open('./.jpg', 'rb') as f:
#     image_part = MIMEImage(f.read())
message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = recipient_email
html_part = MIMEText(body, 'html')
message.attach(html_part)
# message.attach(image_part)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
   server.login(sender_email, sender_password)
   server.sendmail(sender_email, recipient_email, message.as_string())