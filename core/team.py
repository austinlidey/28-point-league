"""Module for NFL Teams.

COPYRIGHT: 
    AuthorChaos / 2023
"""
from typing import Final

from score import NFL_TEAMS, team_is_not_initialized


_BYE_WEEK: Final[int] = -1
_NOT_YET_PLAYED: Final[int] = -2

class Team():
    """Class representing an NFL team with statistical data."""
    name: str
    logo_url: str
    scores_by_week: list
    bye_week_index: int
    score_average: float

    def __init__(self, name, logo_url) -> None:
        self.name = name
        self.logo_url = logo_url
        self.scores_by_week = self._init_weekly_scores()
        self.bye_week_index = -1
        self.score_average = 0.0
    
    def set_week_score(self, index: int, score: int) -> None:
        self.scores_by_week[index] = score

    def _init_weekly_scores(self) -> list[int]:
        return [-1] * 18


def process_week_data(week_data: list[dict]):
    # Range of 12 to 16 games played in a given week.
    current_week: int = week_data['week']['number']
    _process_event_data(current_week, week_data['events'])


def _process_event_data(week_count, event_data):
    for game in event_data:
        # Init/update teams
        game_status = game['status']['type']['name']
        for team in game['competitions'][0]['competitors']:
            cur_team: Team
            team_name = team['team']['name']
            team_logo = team['team']['logo']
            # If the teams not init'd yet, do it first.
            if team_is_not_initialized(team_name):
                NFL_TEAMS[team_name] = Team(name=team_name,
                                            logo_url=team_logo)

            # Populate data for the team now.
            cur_team = NFL_TEAMS.get(team_name)
            week_element = (week_count - 1)
            if game_status == 'STATUS_FINAL':
                cur_team.set_week_score(week_element, int(team['score']))
            elif game_status == 'STATUS_SCHEDULED':
                cur_team.set_week_score(week_element, _NOT_YET_PLAYED)
            else:
                raise ValueError(f'Status message: `{game_status}` is not defined.') 
            
            # Calculate average after all weeks accounted for.
            if week_count == 18:
                _process_avg_score(cur_team)
                _set_team_bye_weeks(cur_team)


def _process_avg_score(team: Team) -> None:
    games_played: int = 0
    total_sum: int = 0
    for score in team.scores_by_week:
        if score != _BYE_WEEK and score != _NOT_YET_PLAYED:
            total_sum += score
            games_played += 1
    team.score_average = float(total_sum / games_played)

def _set_team_bye_weeks(team: Team) -> None:
    for idx, score in enumerate(team.scores_by_week):
        if score == _BYE_WEEK:
            team.bye_week_index = idx