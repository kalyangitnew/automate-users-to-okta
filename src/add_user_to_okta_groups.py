import os
import sys
import requests

def add_user_to_group(user_id, group_name):
    # Your Okta domain and API token
    okta_domain = os.getenv('OKTA_DOMAIN')
    api_token = os.getenv('OKTA_API_TOKEN')

    # The Okta API endpoint for adding a user to a group
    url = f"https://{okta_domain}/api/v1/groups/{group_name}/users/{user_id}"

    # The headers for the API request
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'SSWS {api_token}',
    }

    # Send the API request
    response = requests.put(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        print(f"Successfully added user {user_id} to group {group_name}")
    else:
        print(f"Failed to add user {user_id} to group {group_name}. Response: {response.text}")

if __name__ == "__main__":
    user_id = sys.argv[1]
    group_name = sys.argv[2]
    add_user_to_group(user_id, group_name)