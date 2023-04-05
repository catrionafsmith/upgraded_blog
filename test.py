import requests
import json
response_API = requests.get('https://api.npoint.io/5cb04341e30db4f385c2')
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
# active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print(parse_json[1]["title"])
