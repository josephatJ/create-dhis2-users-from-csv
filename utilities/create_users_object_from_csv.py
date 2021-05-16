
# Josephat Mwakyusa, May 16 2021

import csv

async def get_users_from_csv(file_path):
    users_data= []
    users_file = open(file_path)
    csv_arr_object = csv.reader(users_file)
    next(csv_arr_object)
    for user_data_row in csv_arr_object:
        users_data.append(user_data_row)
    return users_data