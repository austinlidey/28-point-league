import json
import pprint
import requests

# URL to ESPN API endpoint / NOTE: does not have week specified at end!
_WEEKLY_SCOREBOARD: str = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=2023&seasontype=2&week='

def get_raw_data() -> list[dict]:
    """Send GET for NFL score data."""
    score_data: list[dict] = []
    for week_count in range(1, 19):
        generated_url = _WEEKLY_SCOREBOARD + str(week_count)
        # Send GET request to API endpoint.
        get_result = requests.get(url=generated_url)
        # If we get nothing back, just continue.
        if get_result:
            # Parse response in JSON data structure.
            score_data.append(json.loads(get_result.content))
    
    return score_data
