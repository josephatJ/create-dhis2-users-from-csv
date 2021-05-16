import asyncio
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
from utilities.send_users  import create_user

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
        user = {
                "id": users_system_ids[count],
                "firstName": user_row[1],
                "surname": user_row[2],
                "email": "",
                "userCredentials": {
                    "userInfo": { "id": users_system_ids[count] },
                    "username": user_row[3],
                    "password": "Hps.2021",
                    "userRoles": [ {
                    "id": user_row[7]
                    } ]
                },
                "organisationUnits": [ {
                    "id": user_row[11]
                } ],
                "dataViewOrganisationUnits":  [ {
                    "id": user_row[11]
                } ],
                "userGroups": [ {
                    "id": user_row[9]
                } ]
            }
        response = await create_user(user, DEST_BASE_URL,username,password, headers)
        print(response)
            

asyncio.run(main())