"""Driver for 28-point-league notifier.

COPYRIGHT: 
    AuthorChaos / 2023
"""

from data_processing import get_data, populate_teams
from mail import generate_email, send_results_email
from score import week_analysis, NFL_TEAMS


# List of dict's containing weekly NFL data.
regular_season_data = get_data()
# Initialize teams using data.
populate_teams(regular_season_data)
# Run weekly analysis.
week_analysis()
# Generate email template.
subject, body = generate_email()
# Send the email.
assert send_results_email(subject, body), 'Email(s) failed to send.'
