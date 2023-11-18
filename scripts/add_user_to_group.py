import os
import sys
import requests

def add_user_to_group(user_id, group_id):
    okta_domain = os.getenv('OKTA_DOMAIN')
    api_token = os.getenv('OKTA_API_TOKEN')

    url = f"https://{okta_domain}/api/v1/groups/{group_id}/users/{user_id}"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'SSWS {api_token}',
    }

    response = requests.put(url, headers=headers)

    if response.status_code == 200:
        print(f"Successfully added user {user_id} to group {group_id}.")
    else:
        print(f"Failed to add user {user_id} to group {group_id}. Response: {response.text}")

if __name__ == "__main__":
    user_id = sys.argv[1]
    group_id = sys.argv[2]
    add_user_to_group(user_id, group_id)