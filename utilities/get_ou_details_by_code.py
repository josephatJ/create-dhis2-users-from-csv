
# Josephat Mwakyusa, May 16 2021
import json
from requests.auth import HTTPBasicAuth
import requests

async def get_ou_details_by_code(BASE_URL, username,password, code):
    response = requests.get(BASE_URL + '/api/organisationUnits.json?fields=id,name,code&filter=code:eq:' + code, auth=(username,password), verify=False)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['organisationUnits']
    else:
        return None