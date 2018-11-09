# -*- coding: utf-8 -*-
import requests
import json
import sys
from itertools import izip


api_key = sys.argv[1]

app_name_list = []
app_id_list = []

r = requests.get('https://api.newrelic.com/v2/applications.json', headers={
                    'X-Api-Key': api_key, 'Content-Type': 'application/json'})

json_request = json.loads(r.text)

# Creating list name applications
for i in range(len(json_request['applications'])):
    app_name_list.append(json_request['applications'][i]['name'])

# Creating list id applications
for j in range(len(json_request['applications'])):
    app_id_list.append(json_request['applications'][j]['id'])


app_dict = {"data": []}

for app_name, app_id in izip(app_name_list, app_id_list):
    app_dict['data'].append({"{#APPNAME}": app_name, "{#APPID}": app_id})

sys.stdout.write(json.dumps(app_dict))
