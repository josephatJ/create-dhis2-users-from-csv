
# Josephat Mwakyusa, May 16 2021
import json
from requests.auth import HTTPBasicAuth
import requests

async def get_system_ids(BASE_URL, username,password, users_count):
    response = requests.get(BASE_URL + '/api/system/id.json?limit=' + str(users_count), auth=(username,password), verify=False)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['codes']
    else:
        return None