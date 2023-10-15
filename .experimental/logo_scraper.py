"""Script for scraping team logo pictures."""
import json
import os
import re
import requests
import urllib.request
from pathlib import PurePath
from requests import RequestException, Response
from typing import Final

_ALL_32_NFL_TEAMS_URL: Final[str] = \
    'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams?limit=32'


def _download_images() -> bool:
    """Retrieve the logo and store it as <team_name>.png

    Returns:
        bool: True if all were downloaded, False otherwise.
    """
    # Grab the team logo URL's.
    nfl_team_urls = _parse_team_logos()
    # Regex to get team name abbreviation out of URL.
    logo_url_re: re.Pattern = re.compile(r'^\S{42}(?P<team_name>\w{2,3})\S{4}$')
    for team in nfl_team_urls:
        match = logo_url_re.search(team)
        output_filepath: PurePath = PurePath(
            f"./team_logos/{match.groupdict().get('team_name')}.png")
        try:
            if not os.path.exists(output_filepath):
                urllib.request.urlretrieve(team, output_filepath)
        except RuntimeError as err:
            print(f'Failure occurred during logo retrieval:\n{err}')
            return False
    return True


def _parse_team_logos() -> list[str]:
    """Get list of NFL team logo URL's.

    Returns:
        list[str]: URL's to all 32 NFL team logos.
    """
    all_nfl_teams = _parse_team_urls()
    nfl_team_logos: list[str] = []
    # For each team, get their statistics/logos/etc.
    for team_url in all_nfl_teams:
        # Query the end point for our JSON data.
        get_result: Response = requests.get(url=team_url)

        # We want to fail immediately if a bad request occurs; the data is corrupted.
        if get_result.status_code != 200:
            raise RequestException(
                f'The following get-request was unsuccessful: \n{team_url}')    
        # Translate JSON content to dictionary.
        team = json.loads(get_result.content)
        # Add to the return list of team logos.
        nfl_team_logos.append(team['logos'][0]['href'])
    # Verify we have *at least* 32 URL's to a team logo.
    assert len(nfl_team_logos) >= 32, 'Not all NFL team logo URL\'s found.'
    return nfl_team_logos


def _parse_team_urls() -> list[str]:
    """Get list of all NFL team URL's.

    Returns:
        list[str]: URL's to all 32 NFL teams.
    """
    # Query the end point for our JSON data.
    get_result: Response = requests.get(url=_ALL_32_NFL_TEAMS_URL)
    # We want to fail immediately if a bad request occurs; the data is corrupted.
    if get_result.status_code != 200:
        raise RequestException(
            f'The following get-request was unsuccessful: \n{_ALL_32_NFL_TEAMS_URL}')    
    # Translate JSON content to dictionary.
    team_url_list = json.loads(get_result.content)
    # For each team, save the URL.
    url_list: list[str] = []
    for item in team_url_list['items']:
        url = item['$ref']
        url_list.append(url)
    # Verify we have *at least* 32 URL's.
    assert len(url_list) >= 32, 'Not all NFL teams were acquired.'
    return url_list


if __name__ == '__main__':
    _download_images()