import asyncio
import json
#import json
from requests.auth import HTTPBasicAuth
#import requests
from time import sleep

#import base64
# from base64 import b64encode


# Josephat Mwakyusa, May 16 2021

# Reference reading was https://www.linkedin.com/pulse/simplest-way-working-excel-csv-files-python-3-ram-kumar
import csv
import os

# Josephat Mwakyusa, May 16 2021


# import utilities
from utilities.get_server_access import get_user_name_and_password
from utilities.create_users_object_from_csv import get_users_from_csv
from utilities.system_ids  import get_system_ids
from utilities.send_users  import create_user,check_if_user_exist,update_user

# Addresses
DEST_BASE_URL = ''

# authentication
username = ''
password = ''

headers = {
'Content-type': 'application/json'
}

# For user details
users_file_name = ''
users_system_ids = []
users_details = []


existing_users = []
existing_users_headers= ['Names', 'username', 'OU', 'Response']
existing_users.append(existing_users_headers)

async def save_existing_users(rows):
    path = os.getcwd()
    with open(path + '/folder/existing.csv', 'w', encoding='UTF8') as file_to_write:
        writer = csv.writer(file_to_write)
        for row in rows:
            writer.writerow(row)

async def main():
    server_access = await get_user_name_and_password()
    DEST_BASE_URL = server_access['url']
    username = server_access['username']
    password = server_access['password']

    # Get file name from user
    users_file_name =  input("Enter csv file name: ")

    current_directory = os.getcwd()
    users_data = await get_users_from_csv(current_directory + "/" + users_file_name)
    users_system_ids = await get_system_ids(DEST_BASE_URL,username,password, len(users_data))
    # userAndPass = b64encode(b"username:password").decode("ascii")
    # headers['Authorization'] = 'Basic %s' %  userAndPass

    for count,user_row in enumerate(users_data, start=0):
        roles = []
        groups = []
        for role_id in user_row[7].split(","):
            roles.append({
                "id": role_id.replace(" ","")
            })
        for group_id in user_row[9].split(","):
            groups.append({
                "id": group_id.replace(" ","")
            })

        user = {
                "id": users_system_ids[count],
                "firstName": user_row[1],
                "surname": user_row[2],
                "email": "",
                "userCredentials": {
                    "userInfo": { "id": users_system_ids[count] },
                    "username": user_row[3].replace(" ","").replace("  ",""),
                    "password": user_row[10],
                    "userRoles": roles
                },
                "organisationUnits": [ {
                    "id": user_row[11]
                } ],
                "dataViewOrganisationUnits":  [ {
                    "id": user_row[12]
                } ],
                "userGroups":groups
            }
        # Check if user exist
        print(json.dumps(user))
        exist_res = await check_if_user_exist(user, DEST_BASE_URL,username,password, headers)
        print(exist_res)
        if 'users' in exist_res and len(exist_res['users']) > 0:
            # Save on excel the user details
            # response = await update_user(exist_res['users'][0]['id'],user, DEST_BASE_URL,username,password, headers)
            # print('updated')
            # print(response)
            user =[]
            user.append(user_row[1])
            user.append(user_row[3])
            user.append(user_row[11])
            user.append(json.dumps(exist_res['users'][0]))
            existing_users.append(user)
            save_response = await save_existing_users(existing_users)
        else:
            response = await create_user(user, DEST_BASE_URL,username,password, headers)
            print(response)
            

asyncio.run(main())