"""Module for NFL Teams."""

from dataclasses import dataclass


@dataclass
class Team():
    """Class representing an NFL team and associated data."""
    # Name of the team
    name: str
    # List of final score by week, 1 to 18.
    weekly_scores: list
    # Average weekly score to date.
    avg_weekly_score: float

NFL_TEAMS: dict[str, Team] = {}

def populate_teams(games_played: list[dict]) -> None:
    """Parses raw data into Team objects."""
    for game in games_played:
        teams_playing: list = game['competitions'][0]['competitors']
        for team_data in teams_playing:
            # If the team does not exists already, create.
            if not NFL_TEAMS.get(team_data['team']['name'], None):
                NFL_TEAMS[team_data['team']['name']] = Team(
                    name=team_data['team']['name'],
                    weekly_scores=[int(team_data['score'])],
                    avg_weekly_score=float(team_data['score'])
                )
                
            # Team exists, update weekly scores/avg only
            else:
                played = team_data.get('winner', None)
                if played is not None:
                    team = NFL_TEAMS.get(team_data['team']['name'])
                    team.weekly_scores.append(int(team_data['score']))
                    team.avg_weekly_score = float(sum(x for x in team.weekly_scores if isinstance(x, int)) / len(team.weekly_scores))

