import requests
import json
from datetime import datetime, timedelta

app_token = ""  # Socrata app token removed before push (revoke the old one)

# Make a Date ------------
days_of_data_to_get = 2

now = datetime.now()
past_date = (now - timedelta(days=days_of_data_to_get)).strftime("'%Y-%m-%dT%H:%M:%S'")

# requests --------------

url = "https://data.seattle.gov/resource/kzjm-xkqj.geojson?" + "$where=datetime > " + past_date

header = {'X-App-Token': app_token}
resp = requests.request('GET', url=url, headers=header)

with open('fire.json', 'w') as outfile:
    # Method 1: format text and write it
    outfile.write(json.dumps(json.JSONDecoder().decode(resp.text)))

    # Method 2: Dump text as is (with quotes and slashes)
    # json.dump(resp.text, outfile)
