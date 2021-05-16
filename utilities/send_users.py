
# Josephat Mwakyusa, May 16 2021
import json
from requests.auth import HTTPBasicAuth
import requests

async def create_user(payload, DEST_BASE_URL,username,password,headers):
    print("##### Create user")
    # TODO: add support to check is user exists and update accordingly.The update should prompt use to say yes provided user defined the need for prompt actions or otherwise create a csv report for users who existed
    response = requests.post(DEST_BASE_URL + '/api/users', auth = HTTPBasicAuth(username,password), headers=headers, data=json.dumps(payload))
    if response.status_code != 200 and response.status_code != 201:
        print('Failed')
        print(response.status_code)
        return None
    else:
        print("Created successful.........")
        return json.loads(response.content.decode('utf-8'))