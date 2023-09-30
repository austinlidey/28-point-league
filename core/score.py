from fetch_data import get_raw_data
from team import Team, populate_teams, NFL_TEAMS

# Returns all 18 weeks of data.
regular_season_data = get_raw_data()
# For each week, generate Teams and populate associated data.
for week_data in regular_season_data:
    team_list = populate_teams(week_data['events'])
print(NFL_TEAMS)
