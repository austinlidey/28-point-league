import datetime
import json
import requests
from requests import Response, RequestException

from team import process_week_data

# URL to ESPN API endpoint / NOTE: does not have week specified at end!
_CURRENT_YEAR = str(datetime.date.today().year)
_WEEKLY_SCOREBOARD: str = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates={_CURRENT_YEAR}&seasontype=2&week='

def populate_teams(regular_season_data: list[dict]) -> None:
    for week in regular_season_data:
        process_week_data(week)
        

def get_data() -> list[dict]:
    """Get weekly NFL data from ESPN API.

    Raises:
        RequestException: A get-request did not return a status of 200.

    Returns:
        list[dict]: Contain all 18 weeks of NFL stats.
    """
    weekly_nfl_data: list[dict] = []
    for week_count in range(1, 19):
        specific_week_url = _WEEKLY_SCOREBOARD + str(week_count)
        get_result: Response = requests.get(url=specific_week_url)
        
        # We want to fail immediately if a bad request occurs; the data is corrupted.
        if get_result.status_code != 200:
            raise RequestException(
                f'The following get-request was unsuccessful: \n{specific_week_url}')
        # TODO [$6524c1c66067880007969d61]: Create cache of failed get-requests, we can try again.
        
        # Translate content to JSON dictionary.
        weekly_nfl_data.append(json.loads(get_result.content))
    
    assert len(weekly_nfl_data) == 18, f'18 weeks of data not present in {weekly_nfl_data}.'
    return weekly_nfl_data
