"""Module for processing week/score data.

COPYRIGHT: 
    AuthorChaos / 2023
"""
from typing import Final, TYPE_CHECKING

if TYPE_CHECKING:
    from team import Team

_WIN_POINT_REQ: Final[int] = 28

_NO_GAME_PLAYED = 'Week {}: TBD - Not yet played.'
_NO_WINNERS = 'Week {}: ROLLOVER - No teams scored 28 points.'
_DRAW = 'Week {}: ROLLOVER - The following teams scored 28 points {}'
_WINNER = 'Week {}: WINNER - Winning team is {}.'

NFL_TEAMS: dict[str, 'Team'] = {}
WEEKLY_WINNERS: list[str] = []

def team_is_not_initialized(name: str) -> bool:
    return NFL_TEAMS.get(name, None) is None

def week_analysis() -> list:

    for week in range(0, 18):
        week_scores, week_winning_teams = [], []
        for team in NFL_TEAMS.values():
            score = team.scores_by_week[week]
            week_scores.append(score)
            if score == _WIN_POINT_REQ:
                week_winning_teams.append(team)
        inactive_week = all(value == -1 or value == -2 for value in week_scores)

        WEEKLY_WINNERS.append(
            _assess_week_winners(week, week_winning_teams, inactive_week)
            )
    
    return WEEKLY_WINNERS

def _assess_week_winners(week: int, week_winners: list, inactive_week: bool) -> str:
    result = ''
    if len(week_winners) > 1:
        winners_str = _generate_winners_str(week_winners)
        result = _DRAW.format(week, winners_str)
    elif len(week_winners) == 1:
        result = _WINNER.format(week, week_winners[0])
    else:
        if inactive_week:
            result = _NO_GAME_PLAYED.format(week)
        else:
            result = _NO_WINNERS.format(week)

    assert result != '', 'Result of weekly winners assessment was not set.'
    return result

# TODO [$6524c1c66067880007969d63]: Generate HTML email template, then insert data.
def _generate_winners_str(winners: list) -> str:
    result = '\n'
    # TODO [$6524c1c66067880007969d64]: Add size of cash pot to email.
    for winner in winners:
        # TODO [$6524c1c66067880007969d65]: Add images of winning teams using `team.logo_url`.
        result += '\t\t' + winner.name + '\n'
    return result