"""File containing constants for 28 point league.

COPYRIGHT: 
    AuthorChaos / 2023
"""

from typing import Final

# In US Dollars
_LEAGUE_ENTRY_FEE: Final[int] = 90

# 32 Teams in the NFL
_MAX_LEAGUE_POT: Final[int] = _LEAGUE_ENTRY_FEE * 32

# 18 weeks in regular season, league ends at season cut-off
_MAX_WEEKLY_POT: Final[int] = _MAX_LEAGUE_POT / 18