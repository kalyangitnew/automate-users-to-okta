import requests
import json

api_token = "00cs93viqK0z9NjQMzt3jkXDnCQf5QiOnQKbZygwwH"
domain = "dev-10398776.okta.com"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"SSWS {api_token}"
}

# Get the user ID of the existing user
user_id = "00ud63jmtqvUAhNpx5d7"  # Replace with the actual user ID

# Define the group ID where the user will be added
group_id = "00gdbz9l63OBUjKWJ5d7"  # Replace with the actual group ID

url = f"https://{domain}/api/v1/groups/{group_id}/users/{user_id}"
response = requests.put(url=url, headers=headers)

print(response.status_code)
print(response.content)
