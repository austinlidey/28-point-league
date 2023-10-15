"""Module for processing score data.

COPYRIGHT: 
    AuthorChaos / 2023
"""
from typing import Final, TYPE_CHECKING
from week import Week

if TYPE_CHECKING:
    from team import Team


_DRAW: Final[str] = 'The following teams scored 28 points'
_NO_GAME_PLAYED: Final[str] = 'Week has not started/ended yet.'
_NO_WINNERS: Final[str] = 'No teams scored 28 points'
_WIN_POINT_REQ: Final[int] = 28
_WINNER: Final[str] = 'Winning team is'
DETAILED_WEEK_WINNERS: list['Week'] = []
NFL_TEAMS: dict[str, 'Team'] = {}

def team_is_not_initialized(name: str) -> bool:
    return NFL_TEAMS.get(name, None) is None

def week_analysis():

    for week in range(0, 18):
        week_status: 'Week' = Week()
        week_scores, week_winning_teams = [], []
        for team in NFL_TEAMS.values():
            score = team.scores_by_week[week]
            week_scores.append(score)
            if score == _WIN_POINT_REQ:
                week_winning_teams.append(team)
        inactive_week = all(value == -1 or value == -2 for value in week_scores)

        week_status.week_count = (week + 1)
        week_status.week_in_progress = inactive_week
        week_status.winning_teams = week_winning_teams
        _assess_week_winners(week_status, week_winning_teams, inactive_week)
        DETAILED_WEEK_WINNERS.append(week_status)

def _assess_week_winners(week: 'Week', week_winners: list, inactive_week: bool) -> None:
    # TODO [$6524c1c66067880007969d64]: Add size of cash pot to email.
    pot_fate = ''
    result = ''
    if len(week_winners) > 1:
        result = _DRAW
        pot_fate = 'ROLLOVER'
    elif len(week_winners) == 1:
        result = _WINNER
        pot_fate = 'POT RESET'
    else:
        if inactive_week:
            result = _NO_GAME_PLAYED
            pot_fate = "NO CHANGE"
        else:
            result = _NO_WINNERS
            pot_fate = 'ROLLOVER'
    
    week.league_week_status = result
    week.pot_result = pot_fate
