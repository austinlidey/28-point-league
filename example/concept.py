import json
import pprint
import requests

# ESPN API endpoint for standings.
_ESPN_STANDINGS_URL = 'https://cdn.espn.com/core/nfl/standings?xhr=1'
# Send GET request to API endpoint.
get_result = requests.get(url=_ESPN_STANDINGS_URL)
# Parse response in JSON data structure.
json_data_struct = json.loads(get_result.content)

# Colts stats
colts_stats = json_data_struct['content']['standings']['groups'][0]['groups'][2]['standings']['entries'][0]


pprint.pprint(colts_stats)

