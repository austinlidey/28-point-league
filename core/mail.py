"""Send an email containing results of weekly score data.

PRE-REQUISITES:
    - Env variable for email account: 'EMAIL_ACC'
    - Env variable for email app passsord: 'EMAIL_APP_PASSWD'
"""

# Import smtplib for the actual sending function
import os
import smtplib

# Credential initialization
_SENDER = _RECIPIENT = os.getenv('EMAIL_ACC')
_PASSWORD = os.getenv('EMAIL_APP_PASSWD')
assert _SENDER,   'EMAIL_ACC environment variable does not exist.'
assert _PASSWORD, 'EMAIL_APP_PASSWD environment variable does not exist.'

def send_results_email(subject: str, body: str) -> bool:
    """Sends email containing results for given week.

    Args:
        subject (str): The title/subject of the email.
        body (str): The body content of the email.

    Returns:
        bool: True if message was successfully sent. False if unsuccessful.
    """
    assert subject, 'Subject of email cannot be empty.'
    assert body, 'Body content of email cannot be empty.'

    message_sent: bool = False
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(_SENDER, _PASSWORD)
        smtp_server.sendmail(_SENDER, _RECIPIENT, _email_content_generation(subject, body))
        message_sent = True
    
    return message_sent

def _email_content_generation(subject: str, body: str) -> str:
    """Generate formatted string for email communication.

    Args:
        subject (str): The title/subject of the email.
        body (str): The body content of the email.

    Returns:
        str: String formatted for email.
    """
    return f"""Subject:{subject}\n\n{body}"""

# TODO [$6524c1c66067880007969d62]: Create HTML email template, then insert custom data.
def generate_email(weekly_winners: list) -> tuple[str,str]:
    """Generate subject and body components of email.

    Args:
        weekly_winners (list): All winners in the NFL regular season.

    Returns:
        tuple[str,str]: subject and body of email.
    """
    subject = '28 Point League results'
    body = ''
    for week in weekly_winners:
        body += str(week) + '\n\n'
    return subject, body