"""Send an email containing results of weekly score data.

PRE-REQUISITES:
    - Env variable for email account: 'EMAIL_ACC'
    - Env variable for email app passsord: 'EMAIL_APP_PASSWD'

COPYRIGHT: 
    AuthorChaos / 2023
"""
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_format import HTML_BOTTOM_BODY, HTML_MODULAR_BODY, \
    HTML_TOP_BODY, SINGLE_TEAM_CONTAINER
from score import DETAILED_WEEK_WINNERS


# Credential initialization
_SENDER_EMAIL = os.getenv('EMAIL_ACC')
assert os.getenv('EMAIL_LIST'), 'Mailing list environment variable does not exist.'
#TODO: Add cleaner way to switch from debug/default mailing list.
# Currently I use a commented list to switch between debugging and
# actually sending to the mailing list. Could add an argument to 
# simplify this.
_MAILING_LIST = [_SENDER_EMAIL]
# _MAILING_LIST = os.getenv('EMAIL_LIST').split(',')
_PASSWORD = os.getenv('EMAIL_APP_PASSWD')
assert _SENDER_EMAIL,   'EMAIL_ACC environment variable does not exist.'
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

    message_sent: int = 0
    for _RECIPIENT in _MAILING_LIST:
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = _SENDER_EMAIL
        message['To'] = _RECIPIENT

        html_part = MIMEText(body, 'html')
        message.attach(html_part)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(_SENDER_EMAIL, _PASSWORD)
            server.sendmail(_SENDER_EMAIL, _RECIPIENT, message.as_string())
            message_sent += 1

    return len(_MAILING_LIST) == message_sent


def generate_email() -> tuple[str,str]:
    """Generate subject and body components of email.

    Args:
        weekly_winners (list): All winners in the NFL regular season.

    Returns:
        tuple[str,str]: subject and body of email.
    """
    subject = '28 Point League results'
    body = _generate_body()
    return subject, body

def _generate_body() -> str:
    """Wip."""
    body: str = ""
    body += HTML_TOP_BODY
    for week in DETAILED_WEEK_WINNERS:
        team_container = ''
        for team in week.winning_teams:
            team_container += SINGLE_TEAM_CONTAINER.format(team.logo_url, team.name)
        week_status = f'Week {week.week_count}:'
        body += HTML_MODULAR_BODY.format(week_status, week.pot_result, week.league_week_status, team_container)

    body += HTML_BOTTOM_BODY
    body = body.replace('\n', '')
    return body
