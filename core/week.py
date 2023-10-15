"""Module for weekly winner tracking."""
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from team import Team


class Week():
    """Class representing a week in NFL."""
    _week_count: int
    _week_in_progress: bool
    _winning_teams: list['Team']

    def __init__(self) -> None:
        """Create the week object."""
        self._pot_result = ''
        self._league_week_status = ''
        self._week_count = 0
        self._week_in_progress = False
        self._winning_teams = []
    
    @property
    def pot_result(self) -> str:
        return self._pot_result
    
    @property
    def league_week_status(self) -> str:
        return self._league_week_status
    
    @property
    def week_count(self) -> int:
        return self._week_count

    @property
    def week_in_progress(self) -> bool:
        return self._week_in_progress
    
    @property
    def winning_teams(self) -> list['Team']:
        return self._winning_teams
    
    @pot_result.setter
    def pot_result(self, new_result: str) -> str:
        self._pot_result = new_result
    
    @league_week_status.setter
    def league_week_status(self, new_status) -> str:
        self._league_week_status = new_status

    @week_count.setter
    def week_count(self, week_count: int) -> None:
        self._week_count = week_count

    @week_in_progress.setter
    def week_in_progress(self, in_progress: bool) -> None:
        self._week_in_progress = in_progress

    @winning_teams.setter
    def winning_teams(self, new_team_list) -> None:
        self._winning_teams = new_team_list
