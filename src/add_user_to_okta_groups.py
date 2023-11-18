import requests
import json
import os

def add_user_to_okta_groups(user_id, group_ids):
    okta_api_key = os.environ.get('OKTA_API_KEY')
    okta_org_url = os.environ.get('OKTA_ORG_URL')

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'SSWS {okta_api_key}',
    }

    user_url = f'{okta_org_url}/api/v1/users/{user_id}'
    user_response = requests.get(user_url, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()

        for group_id in group_ids:
            add_user_to_group_url = f'{okta_org_url}/api/v1/groups/{group_id}/users'
            payload = {'id': user_data['id']}
            requests.put(add_user_to_group_url, headers=headers, json=payload)

            print(f'User {user_data["profile"]["login"]} added to group {group_id}')
    else:
        print(f'Error: Unable to fetch user details. Status code: {user_response.status_code}')

if __name__ == '__main__':
    user_id = input('Enter the user ID: ')
    group_ids = input('Enter the comma-separated group IDs: ').split(',')

    add_user_to_okta_groups(user_id, group_ids)
