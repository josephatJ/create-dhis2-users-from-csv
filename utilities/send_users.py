
# Josephat Mwakyusa, May 16 2021
import json
from requests.auth import HTTPBasicAuth
import requests

async def check_if_user_exist(payload, DEST_BASE_URL,username,password,headers):
    # .json?filter=userCredentials.username:in:[josephatjulius]
    print("##### check user")
    # TODO: add support to check is user exists and update accordingly.The update should prompt use to say yes provided user defined the need for prompt actions or otherwise create a csv report for users who existed
    response = requests.get(DEST_BASE_URL + '/api/users.json?filter=userCredentials.username:in:[' + payload['userCredentials']['username'] +']', auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print('Failed')
        return None
    else:
        print("User found.........")
        return json.loads(response.content.decode('utf-8'))

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

async def update_user(id,payload, DEST_BASE_URL,username,password,headers):
    print("##### Create user")
    # TODO: add support to check is user exists and update accordingly.The update should prompt use to say yes provided user defined the need for prompt actions or otherwise create a csv report for users who existed
    response = requests.put(DEST_BASE_URL + '/api/users/' + id, auth = HTTPBasicAuth(username,password), headers=headers, data=json.dumps(payload))
    if response.status_code != 200 and response.status_code != 201:
        print('Failed')
        print(response.status_code)
        return None
    else:
        print("Created successful.........")
        return json.loads(response.content.decode('utf-8'))